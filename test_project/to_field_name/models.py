from django.db import models

class Case(models.Model):
    case_num = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(self.case_num)
