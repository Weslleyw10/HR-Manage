from django.db import models

# Create your models here.
class Document(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)