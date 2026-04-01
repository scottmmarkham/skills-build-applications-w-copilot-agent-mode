from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', team='Test Team', type='Running', duration=30)
        self.assertEqual(str(activity), 'testuser - Running')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(str(leaderboard), 'Test Team: 100')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Push Ups', difficulty='Easy')
        self.assertEqual(str(workout), 'Push Ups (Easy)')
