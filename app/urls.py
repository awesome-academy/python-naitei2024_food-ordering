from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('dish-detail', views.DishDetail.as_view(), name='dish-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
