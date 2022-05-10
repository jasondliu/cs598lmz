import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import pymysql
pymysql.install_as_MySQLdb()

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

import django
django.setup()

from blog.models import Category, Tag, Post
from django.contrib.auth.models import User

def populate():

    python_cat = add_cat('Python', views=128, likes=64)

    add_post(cat=python_cat,
        title="Введение в Python",
        author=User.objects.get(username='admin'),
        content="Всем привет. Это мой первый пост на блоге. Я решил начать писать п
