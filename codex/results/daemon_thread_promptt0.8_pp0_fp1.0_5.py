import threading
# Test threading daemon
class myThread():
    def __init__(self):
        self.lock = threading.Lock()
        self.thread_list = []

    def start_wifi(self, name, content):
        self.t = threading.Thread(target=self.wifi_monitor,args=(name, content))
        self.t.setDaemon(True)
        self.t.start()

    def wifi_monitor(self, name, content):
        self.lock.acquire()
        try:
            for i in range(10):
                print i, "  " + name, " ", content
                time.sleep(1)
        finally:
            self.lock.release()


if __name__ == '__main__':
    # 监听wifi信号强度
    # wifi_thread = threading.Thread(target=wifi_monitor,args=())
    # wifi_thread.setDaemon(True)
    # wifi_thread.start()
    thread_list = []
    t = myThread()
    thread_list
