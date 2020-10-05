from django.contrib import admin
from TestModel.models import Truth

# Register your models here.
@admin.register(Truth)
class UserAdmin(admin.ModelAdmin):
    list_display = ('Truth','label','reason')
    def __unicode__(self):
        return self.Truth
