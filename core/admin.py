from django.contrib import admin
from core.models import Evento
# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')  # mostra estas informaçoes
    list_filter = ('titulo',)   # acrescenta filtros


admin.site.register(Evento, EventoAdmin)