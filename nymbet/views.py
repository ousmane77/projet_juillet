from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Championnat, Match,Equipe1,Equipe1_opt,Equipe2,Equipe2_opt,Neutre, UserProfile, Pronostic
# Create your views here.
@login_required
def home(request):
    context = {
        'users':UserProfile.objects.all(),
        'championnats': Championnat.objects.all(),
        'matchs': Match.objects.all(),
        'equipe1': Equipe1.objects.all(),
        'vic1': Equipe1_opt.objects.all(),
        'equipe2': Equipe2.objects.all(),
        'vic2': Equipe2_opt.objects.all(),
        'nul': Neutre.objects.all(),
    }
    return render(request, 'nymbet/home.html', context)


def match(request, id):
    match = get_object_or_404(Match, pk=id)
    context = {
        'match': match,
        'championnats': Championnat.objects.all(),
        'equipe1': Equipe1.objects.all(),
        'option1': Equipe1_opt.objects.all(),
        'equipe2': Equipe2.objects.all(),
        'option2': Equipe2_opt.objects.all(),
        'neutre': Neutre.objects.all(),
        'pronos': Pronostic.objects.all(),
    }
    
    return render(request, 'nymbet/match_detail.html', context)

def championnat(request, id):
    championnat = get_object_or_404(Championnat, pk=id)
    context = {
        'championnat': championnat,
        'championnats': Championnat.objects.all(),
        'match': Match.objects.all(),
        'equipe1': Equipe1.objects.all(),
        'vic1': Equipe1_opt.objects.all(),
        'equipe2': Equipe2.objects.all(),
        'vic2': Equipe2_opt.objects.all(),
        'nul': Neutre.objects.all(),
    }
    
    return render(request, 'nymbet/championnat.html', context)

def documentation(request):
    return render(request, 'nymbet/documentation.html')
	
	
	
