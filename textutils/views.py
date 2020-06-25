# I have created this file - Rakshit

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    purpose = ""
    counter = ""
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Checkbox Value
    removepunc          = request.POST.get('removepunc', 'off')
    fullcaps            = request.POST.get('fullcaps', 'off')
    newlineremover      = request.POST.get('newlineremover', 'off')
    extraspaceremover   = request.POST.get('extraspaceremover', 'off')
    charcounter         = request.POST.get('charcounter', 'off')


    # Check with checkbox is on
    if charcounter == "on":
        purpose = purpose + ' : Number of characters in textfield :'
        counter = 'Number of Characters in textfield are: ' + str(len(djtext))
        params = {
            'purpose': purpose,
            'counter': counter
        }

    if removepunc == "on":
        analyzed = ""
        purpose = purpose + ' : Removed Punctuations : '
        punctuations = '''!()-[]{};:'"\,<>./|?@#$%^&*+_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose': purpose,
            'counter': counter,
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if fullcaps == "on":
        analyzed = djtext.upper()
        purpose = purpose + ' : Changed to UPPERCASE : '
        params = {
            'purpose': purpose,
            'counter': counter,
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        purpose = purpose + ' : Removed New lines : '
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {
            'purpose': purpose,
            'counter': counter,
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        purpose = purpose + ' : Removed New lines : '
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {
            'purpose': purpose,
            'counter': counter,
            'analyzed_text': analyzed
        }

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on":
        return HttpResponse("Please Select at least one Operation any try again.")

    return render(request, 'analyze.html', params)

