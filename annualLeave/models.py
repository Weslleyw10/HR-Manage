from django.db import models

from employee.models import Employee

# Create your models here.
class AnnualLeave(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    reason = models.CharField(max_length=150)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.name)