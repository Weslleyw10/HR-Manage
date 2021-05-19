from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

from departament.models import Departament
from company.models import Company

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=CASCADE)
    name = models.CharField(max_length=150)
    departament = models.ManyToManyField(Departament)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.name)