from django.contrib import admin

from .models import *

## Registring the FTLapp models with admin for interaction
admin.site.register(User)
admin.site.register(ActivityPeriod)

