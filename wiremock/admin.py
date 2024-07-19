from django.contrib import admin
from .models import WiremockStub
from django_json_widget.widgets import JSONEditorWidget
from django.db import models


class WiremockStubAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


admin.site.register(WiremockStub, WiremockStubAdmin)