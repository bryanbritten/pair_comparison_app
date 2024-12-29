from django.shortcuts import render, redirect
from goals.models import GoalPair

def ChoiceChooser(request):
    goal_pair = GoalPair.objects.filter(seen=False).first()
    if not goal_pair:
        return render(request, "goals/completed.html")

    context = {
        "choice1": goal_pair.goal1,
        "choice2": goal_pair.goal2,
    }
    request.session['current_pair_id'] = goal_pair.id
    return render(request, 'goals/main.html', context)

def ChoiceSubmission(request):
    if request.method == 'POST':
        current_pair_id = request.session.get('current_pair_id')

        if current_pair_id:
            pair = GoalPair.objects.get(id=current_pair_id)
            pair.seen = True
            pair.seen()

    return redirect('goals:choices') 