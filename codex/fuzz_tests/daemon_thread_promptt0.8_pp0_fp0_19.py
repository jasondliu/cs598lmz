import threading
# Test threading daemon mode
# To test, create a file test.txt
# In cmd, run this program, then delete test.txt, check the file size on disk, it should not have changed

class Watcher(threading.Thread):
    def __init__(self, file_to_watch, delay, watch_interval, callback):
        self.delay = delay
        self.watch_interval = watch_interval
        self.callback = callback
        self.file_to_watch = file_to_watch
        super(Watcher, self).__init__()

    def check_size(self):
        return os.stat(self.file_to_watch)

    def run(self):
        self.start_time = time.time()
        prev_size = self.check_size()
        while True:
            time.sleep(self.watch_interval)
            cur_size = self.check_size()
            if cur_size != prev_size:
                self.callback()
                prev_size = cur_size
            if (time.time() - self.start_time) >
