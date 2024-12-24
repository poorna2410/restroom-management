"""
URL configuration for restroom_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import include, path
# # from restroom.views import index
# from restroom.views import home

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('restroom/', include('restroom.urls')),
#     # path('', index, name='home'), 
#     path('', home, name='home'),  # Changed to home view
# ]
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restroom.urls')),  # Include the restroom app's URLs at the root
]


