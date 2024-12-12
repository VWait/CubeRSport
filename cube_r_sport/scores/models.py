from django.db import models
from django.contrib.auth.models import User

from tournaments.models import Criteria


class Score(models.Model):
    value = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)