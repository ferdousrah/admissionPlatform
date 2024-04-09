from django.contrib import admin
from .models import Business, PartnerSchool

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('owner_first_name', 'owner_last_name', 'email', 'phone_number', 'source_country')  # Fields to display in the list view
    list_filter = ('preferred_contact_method', 'source_country')  # Filters on the right sidebar
    search_fields = ('owner_first_name', 'owner_last_name', 'email', 'source_country')  # Searchable fields

admin.site.register(Business, BusinessAdmin)

@admin.register(PartnerSchool)
class PartnerSchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'contact_first_name', 'contact_last_name', 'contact_email', 'destination_country')
    search_fields = ('school_name', 'contact_first_name', 'contact_last_name', 'contact_email')
    list_filter = ('destination_country', 'referral_check')