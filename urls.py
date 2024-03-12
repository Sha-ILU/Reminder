from django.urls import path
from .views import RemindView

urlpatterns = [
    path('api/create-reminder/', RemindView.as_view(), name='create-reminder'),
]

