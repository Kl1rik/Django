from django import forms
 
class UserForm(forms.Form):
    choice_group = [("kid","6-12"),("teenager","13-17"),("adult","18+")]
    name = forms.CharField()
    age_group = forms.ChoiceField(choices=choice_group)
    feedback = forms.CharField(widget= forms.Textarea)