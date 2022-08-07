from ResumeApp import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('fileUpload', views.fileUpload, name='fileUpload'),
    path('bookReader', views.bookReader, name='bookReader'),
    path('bookReaderAudio', views.bookReaderAudio, name='bookReaderAudio'),
]