import codecs
codecs.register_error("test", codecs.lookup_error("ignore"))

from opencc import OpenCC

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,errors='test')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer,errors='test')

class CX_Thread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("开始线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release
