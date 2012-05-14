from models import Test, Alternative, LogEntry
from django.contrib import admin


class AlternativeInline(admin.StackedInline):
    model = Alternative
    fields = ('template_name',)
    extra = 2


class TestAdmin(admin.ModelAdmin):
    list_display = ('template_name', 'outcome_summary')
    inlines = (AlternativeInline,)
    list_filter = ('active',)


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('action', 'alternative', 'logged_at')
    readonly_fields = ('action', 'alternative', 'logged_at')

admin.site.register(Test, TestAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
