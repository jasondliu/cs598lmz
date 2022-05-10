import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import json
import logging
import MySQLdb
import warnings
warnings.filterwarnings('ignore', category=MySQLdb.Warning)

from config import config

# =============================================================================
# 
# =============================================================================

def get_conn():
    return MySQLdb.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        user=config.DB_USER,
        passwd=config.DB_PASSWORD,
        db=config.DB_NAME,
        charset='utf8mb4')

def get_cursor(conn):
    return conn.cursor(MySQLdb.cursors.DictCursor)

def close_cursor(cursor):
    cursor.close()

def close_conn(conn):
    conn.close()

def query(sql, args=None):
    conn = get_conn()
    cursor = get_cursor
