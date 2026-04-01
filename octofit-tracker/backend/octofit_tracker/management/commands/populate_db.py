from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

# Import models from octofit_tracker.models
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('All collections cleared.')

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        self.stdout.write(f'Teams created: {Team.objects.count()}')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', first_name='Peter', last_name='Parker'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password', first_name='Diana', last_name='Prince'),
        ]
        self.stdout.write(f'Users created: {User.objects.count()}')

        # Create activities
        Activity.objects.create(user='ironman', team='Marvel', type='Running', duration=30)
        Activity.objects.create(user='spiderman', team='Marvel', type='Cycling', duration=45)
        Activity.objects.create(user='batman', team='DC', type='Swimming', duration=60)
        Activity.objects.create(user='wonderwoman', team='DC', type='Yoga', duration=50)
        self.stdout.write(f'Activities created: {Activity.objects.count()}')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=110)
        self.stdout.write(f'Leaderboard entries created: {Leaderboard.objects.count()}')

        # Create workouts
        Workout.objects.create(name='Push Ups', difficulty='Easy')
        Workout.objects.create(name='Pull Ups', difficulty='Medium')
        Workout.objects.create(name='Squats', difficulty='Easy')
        Workout.objects.create(name='Deadlift', difficulty='Hard')
        self.stdout.write(f'Workouts created: {Workout.objects.count()}')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
