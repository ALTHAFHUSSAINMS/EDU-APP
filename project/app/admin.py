from django.contrib import admin
from .models import student
from .models import college
from .models import ADMIN
from .models import science
from .models import commerce
from .models import literature
from .models import humanities
from .models import finearts
from .models import journalism
from .models import engineering
from .models import law

# Register your models here.
admin.site.register(student)
admin.site.register(college)
admin.site.register(ADMIN)
admin.site.register(science)
admin.site.register(commerce)
admin.site.register(literature)
admin.site.register(humanities)
admin.site.register(finearts)
admin.site.register(journalism)
admin.site.register(engineering)
admin.site.register(law)
