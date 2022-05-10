import socket
import time
import os
import json
import sys

from pympler import tracker

import utils
import settings

# 初始化日志
logger = utils.initLog()

# 初始化tracker
tr = tracker.SummaryTracker()
# 初始化数据库
db = utils.initDB()


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # 初始化日志
        logger = utils.initLog(self.client_address[0], self.client_address[1])
        logger.info('[Get request]')

        # 获取请求
        self.data = self.request.recv(4096).strip()
        if not self.data:
            return
        logger.info('[Request] %s' % self.data)

