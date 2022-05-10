import io
class File(io.RawIOBase):
    def __init__(self, buffer_size=1024*1024, with_thread=True, filename=''):
        self.bufferSize = buffer_size
        self.queue = Queue()
        self.cb_func = None
        self.fd = open(filename, 'wb')
        self.__exit = False
        self.with_thread = with_thread
        if with_thread:
            self.__thread = Thread(target=self.start)
            self.__thread.start()
    def write(self, data):
        if self.with_thread:
            self.queue.put(data)
        else:
            self.fd.write(data)
    def close(self):
        self.__exit = True
        if self.with_thread:
            self.queue.put('')
            self.__thread.join()
        self.fd.close()
    def onFile(self, func):
        self.cb_func = func
    def start(self):
        while not self.__exit:
            if not self.queue.empty():
