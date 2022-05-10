import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 引入数据库连接池
from DBUtils.PooledDB import PooledDB

# 引入配置文件
from config import *

# 定义全局变量
pool = None

# 创建数据库连接池
def get_pool():
    global pool
    if not pool:
        pool = PooledDB(pymysql, mincached=1, maxcached=5, maxshared=5, maxconnections=10, blocking=True,
                        host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    return pool

# 定义查询
def query(sql, args=None):
    # 获取
