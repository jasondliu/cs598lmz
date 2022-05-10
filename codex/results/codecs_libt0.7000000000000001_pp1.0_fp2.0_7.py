import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf-8mb4' else None)
import argparse
import os
import sys
import re
import datetime
import json
import logging
import logging.config
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import log
from db_conn import DBConn

logger = logging.getLogger(__name__)

def format_log_data(log_data):
    if 'id' in log_data:
        log_data['id'] = str(log_data['id'])
    return ','.join([str(v) for v in log_data.values()])

def log_data(data):
    logger.info(format_log_data(data))

def get_user_id(db_conn, name, platform):
    db_conn.execute_sql("select id from user where name=%s and platform=%s", [
