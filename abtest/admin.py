from models import Test, Alternative
from django.contrib import admin


class AlternativeInline(admin.StackedInline):
    model = Alternative
    fields = ('template_name',)
    extra = 2


class TestAdmin(admin.ModelAdmin):
    inlines = (AlternativeInline,)

admin.site.register(Test, TestAdmin)
