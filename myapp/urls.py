from django.urls import path

from .views import index, detail_prod

app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', detail_prod, name='detail_prod'),
]
