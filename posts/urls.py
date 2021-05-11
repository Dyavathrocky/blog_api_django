from django.urls import path

from .views import Postdetail, Postlist


urlpatterns = [
    path('<int:pk>/', Postdetail.as_view()),
    path('', Postlist.as_view()),
]




