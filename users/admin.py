from django.contrib import admin

from users.models import User, SocialAccount

admin.site.register(User)
admin.site.register(SocialAccount)
