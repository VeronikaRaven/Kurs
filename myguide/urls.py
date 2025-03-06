from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from places import views as places_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', places_views.places, name='home'),  # Перенаправление с корня на places
    path('places/', include('places.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='places/login.html', next_page='places'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='places'), name='logout'),
    path('register/', places_views.register, name='register'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

