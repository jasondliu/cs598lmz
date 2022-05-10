from bz2 import BZ2Decompressor
BZ2Decompressor.needs_input = lambda self: not self.unused_data
import re
import sys
import os
import logging
logger = logging.getLogger('log')
sys.path.append('./')
import config
import json
import gzip
import shutil
import time
from datetime import datetime, timedelta

#中文转utf8
def trans_encode(line):
    try:
        return line.decode('gbk').encode('utf-8')
    except:
        try:
            return line.decode('utf-8').encode('utf-8')
        except:
            return line

class ESIndex(object):
    """
    用于执行elasticsearch的增删改查等操作
    仅限单一帐号在初始化时设置,且帐号对应的index需要存在
    """

    def
