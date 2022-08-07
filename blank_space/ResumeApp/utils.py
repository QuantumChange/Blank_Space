import PyPDF2 as pypdf
from gtts import gTTS

def getNumPages(filename = 'sample.pdf'):
    with open(filename, 'rb') as pdf:
        pdfReader = pypdf.PdfFileReader(pdf)
        numPages = pdfReader.numPages
    return numPages


def getBookAudio(filename = 'sample.pdf', pageNo = 1):
    audioFile = 'static/bookReader/audio/audio.mp3'
    with open(filename, 'rb') as pdf:
        pdfReader = pypdf.PdfFileReader(pdf)
        page = pdfReader.getPage(pageNo-1)
        myobj = gTTS(text=page.extractText(), lang='en', slow=False, tld='co.in')
        myobj.save(audioFile)
        return audioFile