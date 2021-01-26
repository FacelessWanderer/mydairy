from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostDetailView, CreatePostView, UpdatePostView, DeletePostView, likeview, CreateCategoryView, categoryview, AddCommentView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='full-post'),
    path('create_post/', CreatePostView.as_view(), name='create-post'),
    path('create_category/', CreateCategoryView.as_view(), name='create-category'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>', categoryview, name='category' ),
    path('like/<int:pk>', likeview, name='like_post'),
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)