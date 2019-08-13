from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')

def count(request):
    data=request.GET['text']
    lst=data.split()
    print(lst)
    wordln=len(lst)
    print(wordln)

    worddict={}
    for word in lst:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
    return render(request,'count.html',{'deepak':data,'total':wordln,'words':worddict.items()})