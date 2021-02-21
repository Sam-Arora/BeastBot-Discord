from django.urls import path

from discord_board import views

urlpatterns = [path("", views.discord_board_index, name="discord_board")]
