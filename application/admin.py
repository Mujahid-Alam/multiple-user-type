from django.contrib import admin
from application.models import *
from django.contrib.auth.models import User, Group
# Register your models here.
# superadmin, admin, administrator, employees, agent 
class AgentAdmin(admin.ModelAdmin):
    list_display =('agent', 'user_id', 'lab_code', 'role',)
    
admin.site.register(Admin)
admin.site.register(Administrator)
admin.site.register(Employee)
admin.site.register(Agent, AgentAdmin)

# ------------------------
admin.site.register(Student)
admin.site.register(Teacher)

# admin.site.unregister(User)
# admin.site.unregister(Group)