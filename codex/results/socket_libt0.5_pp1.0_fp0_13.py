import socket
import struct
import time
import threading
import os
import sys
import subprocess
import json
import cv2
import numpy as np

# 设置编码
type = sys.getfilesystemencoding()

# 新建一个线程
class RecvThread(threading.Thread):
    def __init__(self, threadID, name, sock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.sock = sock

    def run(self):
        print("开始线程：" + self.name)
        while True:
            try:
                # 接收数据
                data = self.sock.recv(1024)
                if data:
                    # 解码
                    data = data.decode(type)
                    print(data)
            except:
                print("接
