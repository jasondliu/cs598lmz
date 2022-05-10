import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import time
from datetime import datetime, date, timedelta
import random
import os

# 数据库位置
# HOST = '127.0.0.1'
# DATABASE = 'test'
# USER = 'root'
# PASSWORD = '123'

# conn = pymysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, charset='utf8mb4')
# cursor = conn.cursor()

post_sql = "INSERT INTO `qr_code_pic` ( `pic_url`, `pic_name`, `pic_size`, `create_time`, `is_deleted`, `creator`, `update_time`, `updator`, `id`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s);"


def save_file
