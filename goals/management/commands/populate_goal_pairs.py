from django.core.management.base import BaseCommand
from goals.models import Goal, GoalPair
from itertools import combinations

class Command(BaseCommand):
    help = 'Populate the GoalPair table with all unique pairs of goals'

    def handle(self, *args, **kwargs):
        # Delete all existing GoalPair records
        GoalPair.objects.all().delete()

        # Reset seen/chosen counts
        Goal.objects.update(times_chosen=0, times_seen=0)

        goals = Goal.objects.all()
        if goals.count() < 2:
            self.stdout.write(self.style.ERROR('Not enough goals to create pairs. Add more goals first.'))
            return

        # Generate all unique pairs of goals
        pair_count = 0
        for goal1, goal2 in combinations(goals, 2):
            # Create the pair only if it doesn't already exist
            _ = GoalPair.objects.create(goal1=goal1, goal2=goal2)
            pair_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully created {pair_count} goal pairs.'))
