from django.shortcuts import render
import  wikipedia

from . import  models

# Create your views here.
def index(request):
    return render(request, "index.html")


def search(request):
    words   = models.Keyword.objects.all()
    quary_t =""
    if request.method == "POST":

        quary = request.POST['search']
        print(f"{request.user} Searched item:", quary)


        keyword_kw = models.Keyword(word=quary, summary= words)
        quary_t =  quary






    return render(request, "analysis.html", {'word':quary_t,  'meaning':words})


