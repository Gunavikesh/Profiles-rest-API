from django.urls import path
from profiles_proj import views


urlpatterns=[
    path('hello-view/',views.HelloAPiView.as_view())
]
