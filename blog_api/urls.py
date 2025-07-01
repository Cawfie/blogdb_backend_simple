from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from blog.views import BlogPostViewSet, CommentViewSet, RegisterView, CustomAuthToken
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', CustomAuthToken.as_view(), name='login'),
    path('api-token-auth/', obtain_auth_token),
]
