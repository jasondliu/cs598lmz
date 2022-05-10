import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

"""
执行shell脚本，初始化数据库，并设置数据库各个表
"""
class Init:
    def __init__(self):
        pass

    def init_db(self):
        table_list = os.listdir("./table")
        table_list.sort()
        for item in table_list:
            shell_command = "sqlite3 -init ./table/{} ./db/xplayer.db {}".format(item, "<./load/init_db.sql")
            os.system(shell_command)

