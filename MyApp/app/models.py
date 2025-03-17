from django.db import models
from django.contrib.auth.models import User
import uuid

class InsuranceInfos(models.Model):
    """Model to store user's insurance information."""
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    bmi = models.FloatField(null=True, blank=True)
    children = models.IntegerField()
    smoker = models.BooleanField()
    region = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='insurance_info')

    def __str__(self):
        """Returns the username of the associated user."""
        return f"{self.user.username}" if self.user else "Unknown User"

    def get_smoker_display(self):
        """Returns 'Oui' (yes) if smoker, 'Non' (no) if not."""
        return "Oui" if self.smoker else "Non"

    def get_sex_display(self):
        """Returns 'Homme' (male) or 'Femme' (female) based on sex."""
        if self.sex == 'male':
            return 'Homme'
        elif self.sex == 'female':
            return 'Femme'

    def get_region_display(self):
        """Returns a readable region name based on the stored region code."""
        if self.region == 'southwest':
            return 'Sud-Ouest'
        elif self.region == 'northeast':
            return 'Nord-Est'
        elif self.region == 'southeast':
            return 'Sud-Est'
        elif self.region == 'northwest':
            return 'Nord-Ouest'

    def get_full_name(self):
        """Returns the full name of the user (first and last name) if available."""
        return f"{self.user.first_name.capitalize()} {self.user.last_name.capitalize()}" if self.user else "Utilisateur inconnu"

class Predictions(models.Model):
    """Model to store predictions made based on the user's insurance information."""
    charges = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    info = models.ForeignKey(InsuranceInfos, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Returns the username of the associated user for the prediction."""
        return self.user.username if self.user else "Utilisateur inconnu"
    
# class Customer (models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     customer_number = models.CharField(max_length=10, unique=True, default=uuid.uuid4().hex[:10].upper())