import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os

# 获取当前文件的路径
pwd = os.path.dirname(os.path.realpath(__file__))

# 定义数据库的连接
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root'
PORT = 3306
DB = 'py_db'
CHARSET = 'utf8mb4'

# 定义数据库连接路径
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(USER, PASSWORD, HOST, PORT, DB, CHARSET)

# 创建数据库引擎
SQLALCHEMY_DAT
