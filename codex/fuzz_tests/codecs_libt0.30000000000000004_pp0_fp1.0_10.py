import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 导入数据库配置
from config import *

# 导入pymysql
import pymysql
pymysql.install_as_MySQLdb()

# 导入django的orm
from django.db import models

# 导入django的认证系统
from django.contrib.auth.models import User

# 导入django的时间模块
from django.utils import timezone

# 导入django的上传文件模块
from django.core.files.storage import FileSystemStorage

# 导入django的图片模块
from PIL import Image

# 导入django的缓存模
