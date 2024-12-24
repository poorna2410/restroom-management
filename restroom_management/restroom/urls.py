from django.urls import path
from . import views  # Import views from the restroom app

urlpatterns = [
    path('', views.home, name='home'),  # Home page shows all restroom statuses
]
