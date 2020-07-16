from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    titolo = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    creato = models.DateTimeField(auto_now_add=True)
    completato = models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField(default=False)
    utente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo
