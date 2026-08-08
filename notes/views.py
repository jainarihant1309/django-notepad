from django.shortcuts import render, redirect, get_object_or_404
from .models import Note


def home(request):

    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:

            Note.objects.create(
                title=title,
                content=content
            )

        return redirect("home")

    notes = Note.objects.all().order_by("-created_at")

    return render(
        request,
        "home.html",
        {
            "notes": notes
        }
    )


def delete_note(request, id):

    note = get_object_or_404(Note, id=id)

    note.delete()

    return redirect("home")


def edit_note(request, id):

    note = get_object_or_404(Note, id=id)

    if request.method == "POST":

        note.title = request.POST.get("title")

        note.content = request.POST.get("content")

        note.save()

        return redirect("home")

    return render(
        request,
        "edit_note.html",
        {
            "note": note
        }
    )


# 1. Unused Code Smell (This function is never used)
def calculate_something_useless(a, b):
    print() # Empty print is a code smell
    return a

# 2. Dead Code Smell (The print line can never run)
def check_status_badly():
    return True
    print("This line will never execute!") 
