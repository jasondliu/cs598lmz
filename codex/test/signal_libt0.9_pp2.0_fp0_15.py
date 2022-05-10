import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class TimeoutException(Exception):
    pass


class Alarm(threading.Thread):
    def __init__(self, sec):
        self.sec = sec
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(self.sec)
