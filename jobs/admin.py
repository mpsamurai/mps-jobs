from django.contrib import admin
from jobs import models

# Register your models here.
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    pass


class LinkInline(admin.TabularInline):
    model = models.Link


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    inlines = [LinkInline, ]
    

@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    pass

