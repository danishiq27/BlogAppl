
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import frontPage, About,robot_txt
from django.contrib.sitemaps.views import sitemap

from .sitemaps import CategorySitemap, PostSitemap

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', robot_txt, name='robot_txt'),
    path('admin/', admin.site.urls),
    path('about/', About, name='about'),
    path('', include('blog.urls')),
    path('', frontPage, name='frontpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
