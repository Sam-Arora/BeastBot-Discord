from django.shortcuts import render
botName = 'BeastBot'
botPrefix = '!'

def home(request):
    args = {}
    args['botName'] = botName
    return render(request, "main.html", args)

def commands(request):
    args = {}
    args['botName'] = botName
    args['botPrefix'] = botPrefix
    return render(request, "commands.html", args)

def about(request):
    args = {}
    args['botName'] = botName
    return render(request, "about.html", args)

def features(request):
    args = {}
    args['botName'] = botName
    return render(request, "features.html", args)