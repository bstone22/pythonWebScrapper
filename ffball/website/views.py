from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        'players': 'Todd Gurley',
    }
    return render(request, 'index.html', context=context)
