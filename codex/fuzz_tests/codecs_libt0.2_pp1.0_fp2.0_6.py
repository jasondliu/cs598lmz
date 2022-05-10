import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 使用pymysql模块
import pymysql
pymysql.install_as_MySQLdb()

# 导入django自带的用户模块
from django.contrib.auth.models import User

# 导入django自带的模块
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# 导入自定义的模块
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('account/', include('account.urls')),
    path('article/', include('article.urls
