from django.shortcuts import render, get_object_or_404, redirect
from .models import CelestialBody, Leaderboard
from .forms import CelestialBodyForm, LeaderboardForm
import random

def index(request):
    if 'planets' not in request.session:
        request.session['planets'] = list(CelestialBody.objects.filter(is_planet=True).values_list('pk', flat=True))
        request.session['correct_answers'] = 0
        request.session['total_questions'] = 0
        random.shuffle(request.session['planets'])

    if request.method == 'POST':
        form = CelestialBodyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            correct_answer = get_object_or_404(CelestialBody, pk=request.session['current_planet_id'])
            if name.lower() == correct_answer.name.lower():
                request.session['correct_answers'] += 1
            request.session['total_questions'] += 1

            if request.session['planets']:
                request.session['current_planet_id'] = request.session['planets'].pop(0)
                return redirect('index')
            else:
                return render(request, 'planets/leaderboard_form.html', {
                    'correct_answers': request.session['correct_answers'],
                    'total_questions': request.session['total_questions']
                })
    else:
        if request.session['planets']:
            request.session['current_planet_id'] = request.session['planets'].pop(0)
            celestial_body = get_object_or_404(CelestialBody, pk=request.session['current_planet_id'])
            form = CelestialBodyForm()
            return render(request, 'planets/result.html', {
                'celestial_body': celestial_body,
                'form': form,
                'correct': None
            })
        else:
            return render(request, 'planets/leaderboard_form.html', {
                'correct_answers': request.session['correct_answers'],
                'total_questions': request.session['total_questions']
            })

def all_planets(request):
    planets = CelestialBody.objects.filter(is_planet=True).order_by('order_from_sun')
    return render(request, 'planets/all_planets.html', {'planets': planets})

def submit_leaderboard(request):
    if request.method == 'POST':
        form = LeaderboardForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            score = request.session['correct_answers']
            Leaderboard.objects.create(name=name, score=score)
            request.session.flush()
            return redirect('leaderboard')
    return redirect('index')

def leaderboard(request):
    leaders = Leaderboard.objects.order_by('-score', 'date')
    return render(request, 'planets/leaderboard.html', {'leaders': leaders})
