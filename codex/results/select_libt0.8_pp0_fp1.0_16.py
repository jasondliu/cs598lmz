import select
import Queue
import logging
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class AsyncActions():
    def __init__(self, strFilePath):
        self.strFilePath = strFilePath
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level = logging.INFO)
        handler = logging.FileHandler("log.txt")
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        # 内容
        self.tasks = Queue.Queue()
        # 线程
        self.threads = []
        # 文件
        self.files = []
        # 标识
        self.flag = 1

    def readFile(self
