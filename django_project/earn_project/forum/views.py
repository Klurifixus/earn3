from django.shortcuts import render

def forum(request):
    # Your view logic here
    return render(request, 'forum/forum.html', context)