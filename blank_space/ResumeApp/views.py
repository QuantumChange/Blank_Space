from fileinput import filename
from telnetlib import STATUS
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ResumeApp import  utils
from django.http import JsonResponse

# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    # print()
    request.session.set_expiry(300)
    return render(request, 'home.html')


# dmy
# dmy12345
def loginUser(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            request.session.set_expiry(300)
            return render(request, 'home.html')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return render(request, 'login.html')


def fileUpload(request):
    context = {}
    request.session.set_expiry(300)
    if request.method == "POST":
        # print(f"request.FILES {request.FILES}")
        # print(f"request.FILES - Files {request.FILES.get('file', False)}")
        if request.FILES.get('file', False):
            handle_uploaded_file(request.FILES.get('file'))
            context = {"File_Upload": "File Upload Successfully"}
        else:
            context = {"File_Upload": "Please select file upload"}

    return render(request, 'fileUpload.html', context)


def handle_uploaded_file(file):
    with open('static/temp/'+file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)



# Book reader view

def bookReader(request):
    context = {}
    context['pageNo'] = range(1,utils.getNumPages('static/bookReader/pdf/sample.pdf')+1)
    return render(request,'bookReader.html',context)

def bookReaderAudio(request):
    if request.method == "POST":
        try:
            pageNo = request.POST.get('pageId')
            filename = utils.getBookAudio('static/bookReader/pdf/sample.pdf', int(pageNo))
            return JsonResponse({'tag':f'<audio controls><source src="{filename}" type="audio/mp3">Your browser does not support the audio element.</audio>'}, status=200)
        except:
            return JsonResponse({'Error': 'Wrong Parameters'}, status=400)
    else:
        return JsonResponse({'Error': 'Wrong Request Type'}, status=400)