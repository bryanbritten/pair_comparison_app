from django.db import models

class Goal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}: {self.description}"
    
class GoalPair(models.Model):
    goal1 = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="goal1_pairs")
    goal2 = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="goal2_pairs")
    seen = models.BooleanField(default=False)

    class Meta:
        unique_together = ('goal1', 'goal2')