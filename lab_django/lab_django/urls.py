"""lab_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import NoteDetailView, NoteListView, NoteCreate, NoteDelete, NoteUpdate
from notes.views import TopicListView, TopicDetailView, TopicCreate, TopicDelete, TopicUpdate

urlpatterns = [
    path('admin/', admin.site.urls),

    path('note/', NoteListView.as_view(), name='note-list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('note/add/', NoteCreate.as_view(), name='note-add'),
    path('note/<int:pk>/update/', NoteUpdate.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDelete.as_view(), name='note-delete'),

    path('topic/', TopicListView.as_view(), name='topic-list'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('topic/add/', TopicCreate.as_view(), name='topic-add'),
    path('topic/<int:pk>/update/', TopicUpdate.as_view(), name='topic-update'),
    path('topic/<int:pk>/delete/', TopicDelete.as_view(), name='topic-delete'),
]
