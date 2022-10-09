from django.core.validators import MinLengthValidator
from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    done = models.BooleanField(default=False)
    description = models.TextField(max_length=200, validators=[MinLengthValidator(3)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
