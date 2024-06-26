from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_proj import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloAPiView.as_view()),
    path('', include(router.urls)),
]
