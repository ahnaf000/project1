from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import os
from . import util
import markdown
from .forms import NewEntryForm
import random



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def querryResult(request, title):
    md = markdown.Markdown()
    check= util.get_entry(title)
    if check is None:
        context = {
            'check': None,
            'title': title,
        }
    else:
        context = {
            'check': 1,
            'entry': md.convert(util.get_entry(title)),
            'title': title,
        }
    return render(request, 'encyclopedia/querryResult.html', context)



def searchResult(request):
    md = markdown.Markdown()
    querry = request.GET.get('q', None)


    if querry is None :
        pass
        context = {
           'querry': querry,
        }
    else:
        check = util.get_entry(querry)
        if check is None:
            #ADD CODE HERE FOR WHEN QUERRY DOESNT MATCH PERFECTLY
            files = []
            for file in os.listdir('entries'):
                files.append(file.rstrip('.md'))

            lis = []
            for file in files:
                if file.lower().startswith(str(querry.lower())) is not False:
                    lis.append(file)

            if len(lis) == 0:
                context={
                    'querry': querry,
                    'check' : None
                }
                return render(request, 'encyclopedia/matchingResult.html',context)
            else:
                context = {
                    'check':1,
                    'matchingResults': lis,
                    'querry': querry
                }
                return render(request, 'encyclopedia/matchingResult.html', context)
            #return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            context = {
                'title': querry,
                'entry': md.convert(check),
                'check': 1
            }
            return render(request,'encyclopedia/querryResult.html', context )


def newEntry(request):

    if request.method == 'POST':
        filled_form = NewEntryForm(request.POST)
        if filled_form.is_valid():
            title = filled_form.cleaned_data['title']
            content = filled_form.cleaned_data['content']
            
            if util.get_entry(title) is None:
                util.save_entry(title,content)
                response = redirect(f"/wiki/{title}")
                return response
            else:
                context = {
                    'title': str(title).capitalize(),
                    'link': f"/wiki/{title}"
                }
                return render(request, 'encyclopedia/fileAlreadyExistsMsg.html', context)
    else:
        form = NewEntryForm()
        context = {
            'form': form
        }
        return render(request, 'encyclopedia/newEntry.html', context)


def randomPage(request):
    allPages = util.list_entries()
    randomPage = str(random.choice(allPages))
    response = redirect(f"/wiki/{randomPage}")
    return response


def editPage(request, title):
    if request.method == 'GET':
        form = NewEntryForm(initial={'title': title,
                                     'content': util.get_entry(title)
                                     })

        if title is not None:
            return render(request, 'encyclopedia/editPage.html', {
                'title': title,
                'form': form,
            })
    else:
        filled_form = NewEntryForm(request.POST)
        if filled_form.is_valid():
            title = filled_form.cleaned_data['title']
            content = filled_form.cleaned_data['content']
            util.save_entry(title, content)
            response = redirect(f"/wiki/{title}")
            return response




def test(request):
    querry = request.GET.get('q', None)


    files = []
    for file in os.listdir('entries'):
        files.append(file.rstrip('.md'))

    lis = []
    for file in files:
        if file.lower().startswith(querry) is not False:
            lis.append(file)
    return HttpResponse(lis)















'''def test(request, article_name):
    return HttpResponse(article_name)

def showEntry(request, ):
    title= request.GET.get('title', None)

    return render(request, 'encyclopedia/searchResult.html',{
        'entry': util.get_entry(title),
        'title': title
    })'''