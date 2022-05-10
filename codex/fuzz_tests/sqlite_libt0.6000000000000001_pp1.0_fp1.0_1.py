import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time
import traceback
import re

# 用于读取配置文件
import ConfigParser

# 加载配置文件
config = ConfigParser.ConfigParser()
config.read('config.ini')

# 获取配置
# 配置路径
path = config.get('config', 'path')
# 配置更新时间
time_interval = config.getint('config', 'time_interval')
# 配置数据库文件
db_file = config.get('config', 'db_file')
# 创建数据库
conn = sqlite3.connect(db_file)
c = conn.cursor()

# 检查数据库是否存在
if not os.path.
