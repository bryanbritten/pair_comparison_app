from django.shortcuts import render, redirect
from goals.models import Goal, GoalPair

def ChoiceChooser(request):
    goal_pair = GoalPair.objects.filter(seen=False).first()
    if not goal_pair:
        goals = Goal.objects.filter(times_chosen__gte=1).order_by("-times_chosen")
        for goal in goals:
            goal.percent_chosen = round(goal.times_chosen / goal.times_seen * 100, 0) if goal.times_seen else 0
        context = {
            "goals": goals,
        }
        return render(request, "goals/completed.html", context)

    context = {
        "choice1": goal_pair.goal1,
        "choice2": goal_pair.goal2,
    }
    request.session['current_pair_id'] = goal_pair.id
    return render(request, 'goals/main.html', context)

def ChoiceSubmission(request):
    if request.method == 'POST':
        selected_choice_id = int(request.POST.get('choice'))
        current_pair_id = request.session.get('current_pair_id')
        
        pair = GoalPair.objects.get(id=current_pair_id)
        pair.seen = True
        pair.save()

        goal1 = Goal.objects.get(id=pair.goal1.id)
        goal1.times_seen += 1
        if goal1.id == selected_choice_id:
            goal1.times_chosen += 1
        goal1.save()

        goal2 = Goal.objects.get(id=pair.goal2.id)
        goal2.times_seen += 1
        if goal2.id == selected_choice_id:
            goal2.times_chosen += 1
        goal2.save()

    return redirect('goals:choices') 