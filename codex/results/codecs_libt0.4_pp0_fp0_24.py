import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 使用pymysql 代替 MySQLdb
import pymysql
pymysql.install_as_MySQLdb()

# 设置默认编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 关闭警告
import warnings
warnings.filterwarnings("ignore")

# 设置日志输出
import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%a, %d %b %Y %H:%M:%S',
    filename = './logs/spider.log',
    filemode = 'w'
