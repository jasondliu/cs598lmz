import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from selenium import webdriver


# 链接数据库
def get_conn():
    """
    :return: 返回数据库连接
    """
    # 1. 创建数据库连接
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="root",
                           # database="toutiao",
                           charset="utf8mb4")

    # 2. 创建游标
    cursor = conn.cursor()

    return conn, cursor


def close_conn(conn, cursor):
    # 关闭游标
    if cursor:
        cursor.close()

    # 关闭数据库连接
    if conn
