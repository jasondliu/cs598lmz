import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import pymysql
pymysql.install_as_MySQLdb()

# 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# 启动Django
import django
django.setup()

# 导入模型
from blog.models import *

# 创建数据
# 创建一个作者
author = Author.objects.create(name='张三', email='zhangsan@163.com')

# 创建一篇文章
article = Article.objects.create(title='第一篇文章', content='文章正文', author=author)

# 为文章添
