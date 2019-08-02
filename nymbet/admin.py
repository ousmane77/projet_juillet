from django.contrib import admin
from .models import Championnat, Equipe1_opt,Equipe2_opt, Neutre, Equipe1, Equipe2, Match, UserProfile, Pronostic

# Register your models here.

admin.site.register(Championnat)
admin.site.register(Equipe1_opt)
admin.site.register(Equipe2_opt)
admin.site.register(Neutre)
admin.site.register(Equipe1)
admin.site.register(Equipe2)
admin.site.register(Match)
admin.site.register(UserProfile)
admin.site.register(Pronostic)
