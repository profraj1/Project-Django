from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    text = request.GET['tA1']
    #print(text)
    wordlist = text.split()
    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedWords = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'text':text,'countWords':len(wordlist),'worddictionary':sortedWords})

def about(request):
    return render(request,'about.html')
