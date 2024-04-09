from django.db import models

class Business(models.Model):
    business_certificate = models.FileField(upload_to='certificates/')
    business_logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    owner_first_name = models.CharField(max_length=100)
    owner_last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    preferred_contact_method = models.CharField(max_length=50)
    how_found = models.CharField(max_length=255)
    referred_by = models.CharField(max_length=255, blank=True, null=True)
    recruiting_year = models.CharField(max_length=4)
    source_country = models.CharField(max_length=100)
    services_provided = models.TextField()

    def __str__(self):
        return f"{self.owner_first_name} {self.owner_last_name}'s Business"
    


class PartnerSchool(models.Model):
    destination_country = models.CharField(max_length=100)
    school_name = models.CharField(max_length=255)
    contact_first_name = models.CharField(max_length=255)
    contact_last_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    contact_title = models.CharField(max_length=255)
    referral_check = models.BooleanField(default=False)
    additional_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.school_name} - {self.contact_first_name} {self.contact_last_name}"

