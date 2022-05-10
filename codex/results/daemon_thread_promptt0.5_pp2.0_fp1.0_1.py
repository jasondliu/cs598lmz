import threading
# Test threading daemon
# https://blog.csdn.net/u010159842/article/details/79259926

# Fix "RuntimeError: There is no current event loop in thread 'Thread-1'."
# https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop

# Fix "RuntimeError: main thread is not in main loop"
# https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop

class Thread(threading.Thread):
    def __init__(self, func, args=()):
        super(Thread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def long_time_task(i):
    print
