from django.contrib import admin
from myfiles.models import Portfolio,Tur,Servise,Team,Murojaat,Saqlash
# Register your models here.

class AdminTur(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Tur,AdminTur)


class AdminPor(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'date','tur','rasm1','vaqt']

admin.site.register(Portfolio, AdminPor)

class AdminServis(admin.ModelAdmin):
    list_display = ['id','nomi','vaqt','malumot','rasm1']

admin.site.register(Servise,AdminServis)


class AdminTeam(admin.ModelAdmin):
    list_display = ['id', 'ism', 'vaqt','malumot','rasm1','lavozim']

admin.site.register(Team, AdminTeam)

class AdminMurojat(admin.ModelAdmin):
    list_display = ['id','name','gmail','title','text','date']

admin.site.register(Murojaat,AdminMurojat)

class AdminSaq(admin.ModelAdmin):
    list_display = ['id','gmail']

admin.site.register(Saqlash,AdminSaq)
