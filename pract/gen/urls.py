from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet, CompanyViewSet, UserViewSet
from rest_framework.authtoken import views

router = DefaultRouter()

router.register(r'applications', ApplicationViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token)
]
