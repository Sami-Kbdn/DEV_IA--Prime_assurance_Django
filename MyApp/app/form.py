from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import InsuranceInfos, Predictions
from django.core.exceptions import ValidationError

# Constants for choices
SEX_CHOICES = [
    ('male', 'Homme'),  # Male
    ('female', 'Femme'),  # Female
]

REGIONS_CHOICES = [
    ('southwest', 'Sud-Ouest'),  # Southwest region
    ('northeast', 'Nord-Est'),  # Northeast region
    ('southeast', 'Sud-Est'),  # Southeast region
    ('northwest', 'Nord-Ouest'),  # Northwest region
]

SMOKER_CHOICES = [
    (True, 'Oui'),  # Yes
    (False, 'Non'),  # No
]

# User Registration Form
class CustomUserCreationForm(UserCreationForm):
    """Form for creating a new user with custom fields."""
    password1 = forms.CharField(
        label="Mot de passe",  # Password
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Confirmation",  # Password confirmation
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    username = forms.CharField(
        label="Nom d'utilisateur",  # Username
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Entrez votre nom d\'utilisateur'})
    )
    last_name = forms.CharField(
        label="Nom",  # Last name
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Entrez votre nom'})
    )
    first_name = forms.CharField(
        label="Prénom",  # First name
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Entrez votre prénom'})
    )
    email = forms.EmailField(
        label="Adresse email",  # Email address
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Entrez votre adresse email'})
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("last_name", "first_name", "email", "password1", "password2")

# Insurance Info Update Form
class InsuranceInfosUpdateForm(forms.ModelForm):
    """Form for updating insurance information."""
    height = forms.FloatField(
        label="Taille (cm)", min_value=50, max_value=250)  # Height in cm
    weight = forms.FloatField(
        label="Poids (kg)", min_value=30, max_value=250)  # Weight in kg
    smoker = forms.ChoiceField(label="Fumeur", choices=SMOKER_CHOICES)  # Smoker choice
    age = forms.IntegerField(label="Votre âge")  # Age
    sex = forms.ChoiceField(label="Genre", choices=SEX_CHOICES)  # Gender
    region = forms.ChoiceField(label="Région", choices=REGIONS_CHOICES)  # Region
    children = forms.IntegerField(label="Nombre d'enfants")  # Number of children

    class Meta:
        model = InsuranceInfos
        fields = ['age', 'sex', 'smoker', 'region', 'children', 'height', 'weight']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Votre âge'}),
            'sex': forms.Select(attrs={'class': 'form-control'}, choices=SEX_CHOICES),
            'region': forms.Select(attrs={'class': 'form-control'}, choices=REGIONS_CHOICES),
            'children': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre d\'enfants'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Votre taille en cm'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Votre poids en kg'}),
            'smoker': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        """Override save method to calculate BMI and save the instance."""
        instance = super().save(commit=False)

        # Calculate BMI if both height and weight are provided
        if self.cleaned_data.get('height') and self.cleaned_data.get('weight'):
            instance.bmi = round(self.cleaned_data['weight'] / ((self.cleaned_data['height'] / 100) ** 2), 2)

        if commit:
            instance.save()
            
        return instance
    
#______________________________________________________________________________
#
# region unused PredictionsForm
#______________________________________________________________________________

class PredictionsForm(forms.ModelForm):
    class Meta():
        fields = ['charges']
        model= Predictions

    charges = forms.IntegerField( label="Prime d'assurance" )
    widgets = { 'charges' : forms.NumberInput(attrs={'class': 'form-control'}) }
    
    def clean_children(self):
        """Validate the number of children."""
        children = self.cleaned_data.get('children')

        if children < 0 or children > 20:
            raise ValidationError("Le nombre d'enfants doit être compris entre 0 et 20.")  # Children must be between 0 and 20
        
        return children
    
    def clean_age(self):
        """Validate the age."""
        age = self.cleaned_data.get('age')

        if age < 18 or age > 120:
            raise ValidationError("L'âge' doit être compris entre 18 et 120.")  # Age must be between 18 and 120
        
        return age
