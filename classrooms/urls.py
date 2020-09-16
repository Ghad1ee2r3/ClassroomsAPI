
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from api import views as api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/',  views.classroom_detail, name='classroom-detail'),
    path('register/', api_views.Register.as_view(), name="api-register"),

     path('login/', TokenObtainPairView.as_view(), name='api-login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('list/' , api_views.ClassroomList.as_view(), name='api-classroom-list'),
    path('detail/<int:classroom_id>' , api_views.ClassroomDetails.as_view(), name='api-classroom-detail'),
    path('update/<int:classroom_id>' , api_views.ClassroomUpdate.as_view(), name='api-classroom-update'),
    path('delete/<int:classroom_id>' , api_views.ClassroomDelete.as_view(), name='api-classroom-delete'),
    path('create/', api_views.ClassroomCreate.as_view(), name='api-classroom-create'),



    path('classrooms/create',  views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/',  views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/',  views.classroom_delete, name='classroom-delete'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
