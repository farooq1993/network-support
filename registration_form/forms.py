from django import forms
from .models import Student, Wireless


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'course_name', 'roll_number', 'email', 'phone_number')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'})
        }



# transport_protocol=(
#     ("Restconf", "Restconf"),
#     ("Netconf", "Netconf"),
#     ("Gnmi", "Gnmi")
# )

class WirelessForm(forms.ModelForm):
    # username=forms.CharField()
    # password=forms.CharField()
    # ipaddress=forms.GenericIPAddressField()
    # tranportprotocol=forms.ChoiceField()
    
    class Meta:
        model=Wireless
        fields="__all__"
        
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password': forms.TextInput(attrs={'class': 'form-control'}),
        #     'ipaddress': forms.TextInput(attrs={'class': 'form-control'}),
        #     'tranportprotocol': forms.TextInput(attrs={'class': 'form-control'}),
            
        # }
  



