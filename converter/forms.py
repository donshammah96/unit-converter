from django import forms

# Form for unit conversion input
class ConversionForm(forms.Form):
    UNIT_CHOICES = [
        ('meters', 'Meters'),
        ('kilometers', 'Kilometers'),
        # Add more units as needed
    ]
    unit_from = forms.ChoiceField(choices=UNIT_CHOICES)  # Field to select the unit to convert from
    unit_to = forms.ChoiceField(choices=UNIT_CHOICES)    # Field to select the unit to convert to
    value = forms.FloatField()                           # Field to input the value to be converted
