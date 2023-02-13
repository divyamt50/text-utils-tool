#i have created this file - Divyam
from django.http import HttpResponse
from django.shortcuts import render


def index(request): 
    return render(request, 'index.html')
    
    
def about(request):
    return render(request, 'about.html')

def analyze(request):
    dj_text = request.POST.get('text','default')
    remove_punc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize', 'off')
    new_line_remove = request.POST.get('newlineremove','off')
    space_remove = request.POST.get('spaceremove','off')
    char_count = request.POST.get('charcount','off')
    
    if remove_punc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove punctuation', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    
    elif capitalize == "on":
        analyzed = ''
        for char in dj_text:
            analyzed = analyzed + char.upper()
        params = {'purpose':'CAPITALIZE', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    
    elif new_line_remove == "on":
        lines = dj_text.splitlines()
        analyzed = " ".join(lines)
        params = {'purpose':'New line remove', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    
    elif space_remove == "on":
        analyzed = ''
        for i in range(len(dj_text)):
            if dj_text[i] == ' ' and dj_text[i + 1] == ' ':
                pass
            else:
                analyzed = analyzed + dj_text[i]
        params = {'purpose':'extra space remove', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    
    elif char_count == "on":
        analyzed = ''
        count = 0
        for char in dj_text:
           count += 1
        analyzed = str(count)
        params = {'purpose':'Character count', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
        
    else:
        return HttpResponse("error")