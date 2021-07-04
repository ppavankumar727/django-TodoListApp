from django.shortcuts import redirect, render
from .models import Note
from django.shortcuts import get_object_or_404


def note_list_view(request):
    to_do_list = Note.objects.filter(finished=False)
    finished_list = Note.objects.filter(finished=True)
    context = {'notes_todo': to_do_list, 'notes_finished': finished_list}
    return render(request, 'note_list.html', context)

    
def finish_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = True
    note.save()
    return redirect('note-list')
