import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello, ")).start()
threading.Thread(target=lambda: sys.stdout.write("world!\n")).start()

# Output: hello,world!
# The newline never gets written by the second thread because stdout is already 
# closed by the first thread.

# It is important to remember that this happens only if multiple threads 
# try to write to the same file-like object. The following code works as you would expect
# instead of writing to sys.stdout, the threads each write to their own file-like object
class LogStream:
    def __init__(self):
        self.lock = threading.Lock()

    def write(self, text):
        self.lock.acquire()
        try:
            sys.stdout.write(text)
        finally:
            self.lock.release()

log_stream = LogStream()
threading.Thread(target=lambda: log_stream.write("hello, ")).start()
threading.Thread(target=lambda: log_stream.write("world!\n")).
