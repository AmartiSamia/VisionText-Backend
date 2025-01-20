from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')  # Afficher ces colonnes dans la liste d'administration
    search_fields = ('name', 'email')      # Ajouter des champs de recherche
    list_filter = ('email',)               # Ajouter un filtre sur le champ email
