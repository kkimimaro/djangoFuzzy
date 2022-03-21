from django.shortcuts import render
# from .recommend import Recommender
from .fuzzyoop import Kernel

kernel = Kernel()


def index(request):
    return render(request, 'index.html')


def result(request):
    if request.method == "POST":
        age = int(request.POST.get("age"))
        length = int(request.POST.get("length"))
        results = kernel.recommendAnime(age, length)
        return render(request, 'result.html', {'results': results})


def admin(request):
    return render(request, 'admin.html')


def admin_search(request):
    if request.method == "GET":
        results = kernel.getAllRules()
        return render(request, 'adm_search.html', {'results': results})



# data = {"title":"a", "year":"b", "genre": "c"}
# rules = [{"age":"baby", "operator": "&", "length":"medium", "rate":"anything"},
#                       {"age":"teen", "operator": "&", "length":"medium", "rate":"amazing"}]
#
# x = kernel.addAnime(data, rules)

def admin_add(request):
    if request.method == "POST":
        data = kernel.getAnimeDataFromRequest(request.POST)
        rules = kernel.getRulesFromRequest(request.POST)

        x = kernel.addAnime(data, rules)
        return render(request, 'adm_add.html')
    elif request.method == "GET":
        return render(request, 'adm_add.html')
