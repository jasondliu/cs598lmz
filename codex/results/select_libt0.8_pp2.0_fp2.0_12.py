import selectors
from datetime import datetime, timedelta
from loguru import logger


# # 全局变量
# # 选择器
# sel = selectors.DefaultSelector()

from utils import get_random_ua, get_proxy


## 从队列中取数据
class Produce:
    def __init__(self, name, queue):
        self.name = name
        self.queue = queue

    # 在一个线程中循环取数据
    def __call__(self, *args, **kwargs):
        while True:
            if not self.queue.empty():
                # 取出队首数据
                data = self.queue.get()
                # 执行
                self.download_request(data)
            # 设置睡眠时间，减小CPU占
