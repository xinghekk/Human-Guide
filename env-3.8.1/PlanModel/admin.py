from django.contrib import admin
from PlanModel.models import Plan
# Register your models here.
@admin.register(Plan)
class UserAdmin(admin.ModelAdmin):
    list_display = ('mission',)
    def __unicode__(self):
        return self.mission
 
