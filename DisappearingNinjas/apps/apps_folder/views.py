from django.shortcuts import render

def index(request):
    url = "static/apps_folder/tmnt.png"
    return render(request, 'apps_folder/index.html', {"url":url})


def ninja(request, color):
    if color == "red":
        url = "/static/apps_folder/red.jpg"
    elif color == "blue":
        url = "/static/apps_folder/blue.jpg"
    elif color == "purple":
        url = "/static/apps_folder/purple.jpg"
    elif color == 'orange':
        url = "/static/apps_folder/orange.jpg"
    else:
        url = "/static/apps_folder/notapril.jpg"
    return render(request, 'apps_folder/index.html', {"url":url})
