from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from notes.models import Note, Topic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class NoteListView(ListView):
    model = Note

class NoteDetailView(DetailView):
    model = Note

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(NoteCreate, self).form_valid(form)

class NoteUpdate(UserPassesTestMixin, UpdateView):
    model = Note
    field = ['title', 'body']

    def test_func(self):
        return self.request.user == self.get_object().created_by

class NoteDelete(UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')

    def test_func(self) -> bool | None:
        return self.request.is_superuser or self.request.user == self.get_object().created_by
    
class TopicListView(ListView):
    model = Topic

class TopicDetailView(DetailView):
    model = Topic

class TopicCreate(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'parent', 'public']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TopicCreate, self).form_valid(form)

class TopicUpdate(UserPassesTestMixin, UpdateView):
    model = Topic
    field = ['title', 'parent', 'public']

    def test_func(self):
        return self.request.user == self.get_object().created_by

class TopicDelete(UserPassesTestMixin, DeleteView):
    model = Topic
    success_url = reverse_lazy('topic-list')

    def test_func(self) -> bool | None:
        return self.request.is_superuser or self.request.user == self.get_object().created_by
