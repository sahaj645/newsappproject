from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import StoryViewSet, CommentViewSet, UserProfileViewSet
from final.views import home_page

router = routers.DefaultRouter()
router.register(r'stories', StoryViewSet, basename='story')
router.register(r'comments', CommentViewSet)
router.register(r'user-profiles', UserProfileViewSet)


urlpatterns = [
     path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('',home_page),
]

