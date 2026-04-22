from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'core'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'core'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'core'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'core'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', first_name='Peter', last_name='Parker'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass', first_name='Clark', last_name='Kent'),
        ]

        # Create activities
        Activity.objects.create(user='ironman', activity_type='Running', duration=30)
        Activity.objects.create(user='spiderman', activity_type='Cycling', duration=45)
        Activity.objects.create(user='batman', activity_type='Swimming', duration=60)
        Activity.objects.create(user='superman', activity_type='Yoga', duration=20)

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', points=100)
        Leaderboard.objects.create(user='spiderman', points=80)
        Leaderboard.objects.create(user='batman', points=90)
        Leaderboard.objects.create(user='superman', points=95)

        # Create workouts
        Workout.objects.create(name='Full Body', description='A full body workout routine')
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        Workout.objects.create(name='Strength Training', description='Build muscle and strength')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))