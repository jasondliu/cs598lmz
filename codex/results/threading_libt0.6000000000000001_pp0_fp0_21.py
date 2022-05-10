import threading
threading.stack_size(1024*1024)


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def main():
    g_var = 100
    g_var_lock = threading.RLock()

    def work1(n):
        g_var_lock.acquire()
        for i in range(n):
            g_var += 1
            print(threading.current_thread(), g_var)
        g_var_lock.release()

    def work2(n):
        g_var_lock.acquire()
        for i in range(n):
            g_var += 10
            print(threading.current_thread(), g_var)
        g_var_lock.
