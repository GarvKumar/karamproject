from django.contrib import admin
from myapp.models import Enquiry
from myapp.models import Complaint
from myapp.models import Feedback

# Register your models here.

admin.site.register(Enquiry)
admin.site.register(Complaint)
admin.site.register(Feedback)