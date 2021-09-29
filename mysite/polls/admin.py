from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Electeur

admin.site.register(Question)
admin.site.register(Electeur)