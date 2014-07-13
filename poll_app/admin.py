from django.contrib import admin

from .models import PollQuestion,PollChoice, VoteTracker


class PollChoiceAdmin(admin.TabularInline):
    model = PollChoice
    
class PollQuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('PollName', {'fields': ['name']}),
                 ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
                ]

    inlines = [PollChoiceAdmin]
    list_display = ('name','pub_date')
    list_filter = ['pub_date']
    search_fields = ['name']

admin.site.register(PollQuestion, PollQuestionAdmin)
admin.site.register(VoteTracker)


