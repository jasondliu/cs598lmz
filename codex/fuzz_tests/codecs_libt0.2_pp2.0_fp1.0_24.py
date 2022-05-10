import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 使用pymysql模块
import pymysql
pymysql.install_as_MySQLdb()

# 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# 启动Django
import django
django.setup()

# 导入模型
from blog.models import Article

# 创建数据
Article.objects.create(title='第一篇文章', content='第一篇文章的内容')
Article.objects.create(title='第二篇文章', content='第二篇文章的内容')
Article.objects.create(title
