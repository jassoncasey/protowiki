from django.contrib import admin
from core.models import Protocol
from core.models import Relation

class ProtocolAdmin(admin.ModelAdmin):
  list_display = ('name', 'layer')

class RelationAdmin(admin.ModelAdmin):
  list_display = ('protocol', 'payload')

# Register your models here.
admin.site.register(Protocol, ProtocolAdmin)
admin.site.register(Relation, RelationAdmin)
