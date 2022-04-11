from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('all-news', views.all_news, name="all-news"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('all-category', views.all_category, name="all-category"),
    path('category/<int:id>', views.category, name="category"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
