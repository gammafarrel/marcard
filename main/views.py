from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'type': 'Celestials',
        'description': 'Zeus',
        'power' : '100',
        'title' : 'MARCARD',
        'name' : 'Gamma Farrel',
        'class' : 'PBP-E',
    }
    return render(request, "main.html", context)
