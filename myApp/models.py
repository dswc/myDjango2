from django.db import models

class student(models.Model):
    cName = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.cName
