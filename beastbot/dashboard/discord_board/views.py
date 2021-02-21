from django.shortcuts import render


def discord_board_index(request):
    return render(request, "index.html", {})
