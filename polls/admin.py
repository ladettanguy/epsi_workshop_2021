# Register your models here.
from django.contrib import admin

from .models import Electeur, Candidat, Block

admin.site.register(Block)
admin.site.register(Electeur)
admin.site.register(Candidat)