from django.shortcuts import render


def base(request, name):
    context = {
        'name': name
    }
    return render(request, 'app/home.html', context)
