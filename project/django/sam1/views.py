from django.shortcuts import render
def home(request):
    return render(request,"home.html",{})
def about(request):
    return render(request,"about.html",{})
def count(requests):
    fulltext=requests.GET['text']
    word_count=len(fulltext.split())
    word_dict={}

    for w in fulltext.split():
        if w in word_dict:
            word_dict[w]+=1
        else:
            word_dict[w]=1
    list=[(i,word_dict[i]) for i in word_dict]
    return render(requests,"count.html",{'fulltext':fulltext,'word_count':word_count,'word_dict':word_dict,'list':list})
