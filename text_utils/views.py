from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def analyze(request):
    text1 = request.POST.get('textbox1')
    cb1 = request.POST.get('cb1')
    cb2 = request.POST.get('fullc', 'off')
    cb3 = request.POST.get('newline', 'off')
    cb4 = request.POST.get('charcount', 'off')
    if cb1 == 'on':
        analyzed_text = ''
        punct = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in text1:
            if char not in punct:
                analyzed_text = analyzed_text + char

        params = {'analyzed_text': analyzed_text}
        text1 = analyzed_text

    if cb2 == 'on':
        analyzed_text = text1.upper()
        params = {'analyzed_text': analyzed_text}
        text1 = analyzed_text

    if cb3 == 'on':
        analyzed_text = ''
        punct = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in text1:
            if char != '\n':
                analyzed_text = analyzed_text + char
        params = {'analyzed_text': analyzed_text}
        text = analyzed_text

    if cb4 == 'on':
        c = 0
        analyzed_text = ''
        for char in text1:
            if char != '\n' and char != ' ':
                c = c + 1;

        params = {'cstmt': 'no of characters are :', 'analyzed_text': text1,
                  'count': c}

    if cb1 == 'on' or cb2 == 'on' or cb3 == 'on' or cb4 == 'on':
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('error')
