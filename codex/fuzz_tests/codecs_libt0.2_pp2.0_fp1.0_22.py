import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 使用pymysql模块
import pymysql
pymysql.install_as_MySQLdb()

# 导入Django默认的设置
import django
django.setup()

# 导入定时任务模块
from apscheduler.schedulers.background import BackgroundScheduler
# 导入时区设置模块
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
# 导入作业模块
from spider.views import get_news_detail

# 实例化调度器
scheduler = BackgroundScheduler()
# 设置定时任
