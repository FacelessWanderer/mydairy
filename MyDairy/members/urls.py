from django.urls import path
from .views import UserRegisterView, PasswordsChangeView, UserEditView, EditProfilePageView, ShowProfilePage, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('initial_settings/', CreateProfilePageView.as_view(), name='initial_settings'),
    path('<int:pk>/profile/', ShowProfilePage.as_view(), name='my_profile'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='password'),
    path('password_success/', views.password_success, name='password_success'),




    path('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#template_name="registration/password_reset.html"
#template_name="registration/password_reset_sent.html"
#template_name="registration/password_reset_form.html"
#template_name="registration/password_reset_done.html"