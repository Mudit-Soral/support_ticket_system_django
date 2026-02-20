from django import forms
from .models import Ticket
from django.contrib.auth.models import User

class TicketForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(is_staff= True)

        if User and not User.is_staff:
            self.fields.pop('assigned_to')
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status', 'progress', 'assigned_to']
    def clean(self):
        cleaned_data= super().clean()

        status = cleaned_data.get('status')
        progress = cleaned_data.get('progress')

        if status == 'OPEN' and progress !=0:
            raise forms.ValidationError("Open tickets must have prgress 0%")
        if status =='IN_Progress' and (progress <=0 or progress >= 100):
            raise forms.ValidationError("In progress tickets must be between 1 and 99%")
        if status == 'RESOLVED' and progress != 100:
            raise forms.ValidationError("Resolved or Closed tickets must have progress 100%")
        return cleaned_data