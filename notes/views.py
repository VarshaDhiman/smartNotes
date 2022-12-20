
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from .models import Notes
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin


class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = 'smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(LoginRequiredMixin, UpdateView):

    model = Notes

    success_url = 'smart/notes'
    form_class = NotesForm


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    login_url = "/admin"
    template_name = "notes/notes_list.html"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_detail.html"


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = 'smart/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
