from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from staff.views import TeamDetail, TeamInfo, about, ServicesList, ServicesUpdateDestroy, ReviewList, ReviewUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/team/', TeamDetail.as_view()),
    path('api/team/<int:pk>/', TeamInfo.as_view()),


    path('api/services/', ServicesList.as_view()),
    path('api/services/<int:pk>/', ServicesUpdateDestroy.as_view()),


    path('api/review/', ReviewList.as_view()),
    path('api/review/<int:pk>/', ReviewUpdateDestroy.as_view()),

    path('', include('staff.urls')),
    path('about/', about, name='about'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
