from django.shortcuts import render
from django.http import HttpResponse
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def test(request, article_name):
    return HttpResponse(article_name)

def showEntry(request, ):
    title= request.GET.get('title', None)

    return render(request, 'encyclopedia/searchResult.html',{
        'entry': util.get_entry(title),
        'title': title
    })