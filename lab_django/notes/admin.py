from django.contrib import admin

from notes.models import Note
from notes.models import Topic

admin.site.register(Note)
admin.site.register(Topic)