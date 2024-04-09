from django import forms

class BusinessForm(forms.Form):
    business_certificate = forms.FileField(
        label='Business Certificate',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': '.pdf, .doc, .docx'}),
        required=False
    )
    business_logo = forms.ImageField(
        label='Business Logo (optional)',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
        required=False
    )
    owner_first_name = forms.CharField(
        label="Owner's First Name",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    owner_last_name = forms.CharField(
        label="Owner's Last Name",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )
    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
        required=True
    )
    preferred_contact_method = forms.ChoiceField(
        label='Preferred Contact Method',
        choices=[('Call', 'Call'), ('SMS', 'SMS'), ('Email', 'Email')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    how_found = forms.CharField(
        label='How did you find out about Admission Platform?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    referred_by = forms.CharField(
        label='Has anyone at Admission Platform referred you? If yes, who? (optional)',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    recruiting_year = forms.CharField(
        label='In which year did you begin recruiting students?',
        widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '\\d{4}', 'placeholder': 'yyyy'}),
        required=True
    )
    source_country = forms.CharField(
        label='Please specify the main source country of your students',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    services_provided = forms.CharField(
        label='What services do you provide to your clients?',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=True
    )
