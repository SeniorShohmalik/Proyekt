from django.contrib import admin
from django.urls import path

from .views import home ,chapter,khadis,search

urlpatterns = [
    path('',home ,name = 'home'),
    path('admin/', admin.site.urls),
    path("chapter/<str:book_name>/",chapter, name='chapter'),
    path('parcha/<str:khadis>/',khadis, name='parcha'),
    path('search/',search ,name='search')
]