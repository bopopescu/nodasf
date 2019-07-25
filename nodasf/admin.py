from django.contrib import admin

from .models import County, Venue, Agency, Genre, Issue, City, Party, Level, Event, Politician, Media_Org, Journalist, Local_Link, STF, STF_Hub, STF_Link, District, Category

class Media_OrgAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'county', 'imageQ']

admin.site.register(County)
admin.site.register(Venue)
admin.site.register(Agency)
admin.site.register(Genre)
admin.site.register(Issue)
admin.site.register(City, CityAdmin)
admin.site.register(Party)
admin.site.register(Level)
admin.site.register(Event)
admin.site.register(Politician)
admin.site.register(Media_Org, Media_OrgAdmin)
admin.site.register(Journalist)
admin.site.register(Local_Link)
admin.site.register(STF)
admin.site.register(STF_Hub)
admin.site.register(STF_Link)
admin.site.register(District)
admin.site.register(Category)