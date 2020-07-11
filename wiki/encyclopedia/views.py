from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def searchResult(request, title):
    title = request.POST['q']
    submitBtn = request.POST['submitBtn']


    return render(request, "encyclopedia/searchResult.html",{
        'entry': util.get_entry(title),
        'title': title
    })
