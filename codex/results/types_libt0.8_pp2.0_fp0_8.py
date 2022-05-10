import types
types.ModuleType('pymysql')

import pymysql
pymysql.install_as_MySQLdb()

# 将当前项目所在路径加入 Python 的环境变量中
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 执行 Django 项目的初始化
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()
