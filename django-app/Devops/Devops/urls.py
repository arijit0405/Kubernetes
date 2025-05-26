from django.contrib import admin
from django.urls import path, include  # ✅ include must be imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demo.urls')),  # ✅ this line uses include
]
