from django.contrib import admin
from .models import IndividualBanks, LegalBanks


admin.site.register(IndividualBanks)
admin.site.register(LegalBanks)