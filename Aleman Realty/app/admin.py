from django.contrib import admin
from .models import ContactForm, HomeListing


admin.site.register(ContactForm)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('first_name')


admin.site.register(HomeListing)
