from django.db import models
from django.contrib.auth.models import User

# Команды
class Team(models.Model):
    city = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    robot_name = models.CharField(max_length=100)
    user_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leader_teams")
    head_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Участники команды
class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="members")
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

# Турниры
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    dt_beg = models.DateTimeField()
    dt_end = models.DateTimeField()

    def __str__(self):
        return self.name

# Связи пользователей с турнирами
class UserTournament(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

# Испытания
class Challenge(models.Model):
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

# Категории
class Criteria(models.Model):
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    max_value = models.IntegerField()
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)