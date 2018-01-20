from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Audience

class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Audience)

admin.site.register(Audience, MyAdmin)
