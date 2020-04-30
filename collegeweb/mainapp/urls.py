from django.urls import path , include

urlpatterns = [
    path('college/', include('web.urls')),
    path('student/', include('student.urls')),
    path('faculty/', include('faculty.urls')),
]
