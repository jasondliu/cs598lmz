import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 添加项目路径
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, '..'))

# 加载配置文件
import conf
conf.load_conf(os.path.join(BASE_DIR, 'conf/db.conf'))

# 载入相关库
from lib import log
from lib import mysql
from lib import redis
from lib import mongo

def run_mysql_query(query, args=None, fetch=True):
    """执行查询
    """
    conn = mysql.connection()
    cursor = conn.cursor(cursor=DictCursor)
    try:
