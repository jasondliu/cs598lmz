import ctypes
import ctypes.util
import threading
import sqlite3
import socket
import os

sqlite_path = '/var/www/html/data.db'

def getdata(id, num_items):
    outstr = ""
    conn = sqlite3.connect(sqlite_path)
    cursor = conn.cursor()
    sql = "SELECT * FROM node{0} WHERE row_num > {1} AND row_num <= {2};".format(id, num_items - 25, num_items)
    values = cursor.execute(sql)
    for row in values:
        for col in row:
            outstr += "{0}\t".format(col)
        outstr += "\n"
    return outstr

def response_get(message):
    id = str(message.split(' ')[1])
    num_items = str(message.split(' ')[2])
    resp = getdata(int(id), int(num_items))
    return resp


def response_max(message):
    id = str(message.split(' ')[1])
