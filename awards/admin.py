from django.contrib import admin
from awards.models import User,Project,Rating,Profile
# Register your models here.
admin.site.register(User)
admin.site.register(Rating)
admin.site.register(Project)
admin.site.register(Profile)