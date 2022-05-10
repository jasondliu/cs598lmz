import threading
threading.Event()

class QThread(threading.Thread):
    def __init__(self, _func, *args, **kwargs):
        super(QThread, self).__init__()
        self.__func = _func
        self.__args = args
        self.__kwargs = kwargs
        self.__result = None

    def run(self):
        self.__result = self.__func(*self.__args, **self.__kwargs)

    def get_result(self):
        try:
            return self.__result  # 如果子线程不使用join方法，此处可能会报没有self.__result的错误
        except Exception:
            return None


def no_blocking_func(func, *args, **kwargs):
    q_thread = QThread(func, *args, **kwargs)
    q_thread.setDaemon(True)
    q_thread.start()
    return
