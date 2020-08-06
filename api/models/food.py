from django.db import models

from .user import User

# Create your models here.
class Food(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  carb = models.DecimalField(max_digits=19, decimal_places=1)
  fat = models.DecimalField(max_digits=19, decimal_places=1)
  protein = models.DecimalField(max_digits=19, decimal_places=1)
  owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"{self.name}s have {self.carb}c {self.fat}f {self.protein}p"

  def as_dict(self):
    """Returns dictionary version of Food models"""
    return {
        'id': self.id,
        'name': self.name,
        'carb': self.carb,
        'fat': self.fat,
        'protein': self.protein
    }
