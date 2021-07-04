from django.shortcuts import redirect, render
from .models import Note
from django.shortcuts import get_object_or_404
from .forms import NoteModelForm


def note_list_view(request):
    form = NoteModelForm
    if(request.method == "POST"):
        form = NoteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note-list')
    to_do_list = Note.objects.filter(finished=False)
    finished_list = Note.objects.filter(finished=True)
    context = {'notes_todo': to_do_list, 'notes_finished': finished_list, "form": form}
    return render(request, 'note_list.html', context)

    
def finish_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = True
    note.save()
    return redirect('note-list')


def delete_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('note-list')


def recover_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = False
    note.save()
    return redirect('note-list')

