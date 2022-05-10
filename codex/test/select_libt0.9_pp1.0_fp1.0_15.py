import select
import sys
import threading
from threading import Thread


host_name = '145.24.222.121'
host_port = 6000
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global exitFlag
