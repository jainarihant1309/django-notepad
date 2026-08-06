from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),

    path("delete/<int:id>/", views.delete_note, name="delete_note"),

    path("edit/<int:id>/", views.edit_note, name="edit_note"),
]