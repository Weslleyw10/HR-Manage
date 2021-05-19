from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, help_text="Company name")

    def __str__(self):
        return str(self.name)