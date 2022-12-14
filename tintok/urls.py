"""tintok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

from video.api.router import router_video
from comment.api.router import router_comment
from users.api.router import router_user
from follow.api.router import router_follow
from notification.api.router import router_notification

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router_user.urls)),
    path('api/', include('users.api.router')),
    path('api/', include(router_video.urls)),
    path('api/', include('video.api.router')),
    path('api/', include(router_comment.urls)),
    path("api/", include(router_follow.urls)),
    path("api/", include("follow.api.router")),
    path("api/", include(router_notification.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
