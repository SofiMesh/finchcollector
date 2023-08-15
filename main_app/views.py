from django.shortcuts import render

finches = [
    {'name': 'Nina', 'classification': 'house_finch', 'description': 'small-bodied finch with fairly large beak and somewhat long, flat head', 'age': 1},
    {'name': 'Lily', 'classification': 'europian goldfinch', 'description': 'small passerine bird', 'age': 2},
]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })