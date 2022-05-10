import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys

# 定义函数：判断是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# 定义函数：获取数据库连接
def get_db_conn():
    conn = MySQLdb.connect(
        host='192.168.5.165',
        port=3306,
        user='root',
        passwd='data~secret!',
        db='test',
        charset='utf8'
    )
    return conn

# 定义函数：关
