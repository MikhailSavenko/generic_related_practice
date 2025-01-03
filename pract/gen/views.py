from rest_framework.viewsets import ModelViewSet
from .models import Application, Company, Favorite, User
from .serializers import ApplicationSerializer, CompanySerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Exists, OuterRef


class ManageFavorite:

    def annotate_qs_is_favorite_field(self, request, queryset):
        if request.user.is_authenticated:
            is_favorite_subquery = Favorite.objects.filter(
                object_id=OuterRef('pk'),
                content_type=ContentType.objects.get_for_model(queryset.model),
                user=request.user
            )
            queryset = queryset.annotate(is_favorite=Exists(is_favorite_subquery))
        return queryset

    @action(methods=['get'], detail=True, permission_classes=[IsAuthenticated])
    def favorite(self, request, pk):
        instance = self.get_object()
        content_type = ContentType.objects.get_for_model(instance)
        favorite_obj, created = Favorite.objects.get_or_create(
            object_id=instance.id,
            content_type=content_type,
            user=request.user
        )
        if created:
            return Response(data={"message": "Контент добавлен в избранное"}, status=status.HTTP_201_CREATED)
        else:
            favorite_obj.delete()
            return Response(data={"message": "Контент удален из избранного"}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False, permission_classes=[IsAuthenticated])
    def favorites(self, request):
        queryset = self.get_queryset().filter(is_favorite=True)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ApplicationViewSet(ModelViewSet, ManageFavorite):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset_annotate_is_favorite = self.annotate_qs_is_favorite_field(queryset=self.queryset, request=self.request)
        return queryset_annotate_is_favorite
    
    
class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


