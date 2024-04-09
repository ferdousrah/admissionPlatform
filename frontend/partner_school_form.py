from django import forms

class PartnerSchoolForm(forms.Form):
    # Assuming dynamic choices for destination_country will be set in the view
    destination_country = forms.ChoiceField(choices=[], label='Destination Country*', required=True)
    school_name = forms.CharField(label='School Name*', max_length=255, required=True)
    contact_first_name = forms.CharField(label='Contact First Name*', max_length=255, required=True)
    contact_last_name = forms.CharField(label='Contact Last Name*', max_length=255, required=True)
    contact_email = forms.EmailField(label='Contact Email*', required=True)
    phone_number = forms.CharField(label='Phone Number', max_length=20, required=False)
    contact_title = forms.CharField(label='Contact Title*', max_length=255, required=True)
    referral_check = forms.BooleanField(label='Check if you have been referred by someone in Admission Platform', required=False)
    additional_comments = forms.CharField(label='Any additional comments:', widget=forms.Textarea(attrs={'rows': 3}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['destination_country'].choices = [
            ('', '-- Select an Item --'),
            ('Australia', 'Australia'),
            ('Canada', 'Canada'),
            ('New Zealand', 'New Zealand'),
            ('United Kingdom', 'United Kingdom'),
            ('United States', 'United States'),
            # Add more choices as needed
        ]
