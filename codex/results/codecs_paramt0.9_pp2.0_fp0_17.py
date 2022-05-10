import codecs
codecs.register_error('replace_space', codecs.replace_error)
import pymysql
from urllib.parse import urlparse
from constant import Configure


class MySQLConnector(object):
    # 打印log
    @staticmethod
    def print_log(prefix, message, is_thread=False):
        res = "[{0}] [{1}] {2}".format(prefix, datetime.datetime.now(), message)
        stream = sys.stdout if not is_thread else sys.stderr
        stream.write(res + '\n')

    # 静态方法：连接数据库
    @staticmethod
    def connect_db(db_name):
        # 打开数据库连接
        conn = pymysql.connect(Configure.MYSQL_ADDR, #Configure.MYSQL_ADDR,Configure.MYSQL_USER,Configure.MYSQL_PASSWORD, db=db_name)
