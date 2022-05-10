import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import pymysql
pymysql.install_as_MySQLdb()

# 设置系统默认编码格式
# reload(sys)
# sys.setdefaultencoding('utf-8')

# 设置Django运行所依赖的环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# 启动Django，作为一个独立的Web服务器
application = get_wsgi_application()
