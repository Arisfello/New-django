from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Lets Learn python!'},
    {'id': 2, 'name': 'Design with me!'},
    {'id': 3, 'name': 'Frontend developers!'},
]


def home(request):
    context = {'room': rooms}
    return render(request, 'home.html', context)


def room(request):
    return render(request, 'room.html')
