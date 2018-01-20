from django.contrib import admin

from .models import Audience

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


@admin.register(Audience)
class AudienceAdmin(TreeAdmin):
    form = movenodeform_factory(Audience)
