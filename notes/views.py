from django.shortcuts import render
from .models import Note


def note_list_view(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'notes/note_list.html', context)
