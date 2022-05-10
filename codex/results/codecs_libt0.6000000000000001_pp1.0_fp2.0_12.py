import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
sys.path.insert(0, '..')

from datetime import datetime, timedelta
import mysql.connector
from tqdm import tqdm
from time import time

from config import *
from lib import *

now = datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

cursor.execute('SET NAMES utf8mb4')
cursor.execute("SET CHARACTER SET utf8mb4")
cursor.execute("SET character_set_connection=utf8mb4")

sql = 'SELECT id, `name`, `url`, is_done, `timestamp` FROM `%s` ORDER BY id DESC' % table_name
cursor.execute(sql)

rows = cursor.fetchall()

for row in
