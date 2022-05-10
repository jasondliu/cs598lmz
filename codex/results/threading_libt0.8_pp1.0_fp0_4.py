import threading
threading.stack_size(67108864) # 64MB stack

def fibonacciNum(n):
    x = 0
    y = 1
    for num in range(0,n):
        temp = x
        x = y
        y = temp + y
    return x

# Start a thread with a specific stack size
thread = threading.Thread(target=fibonacciNum, args=(10,))
thread.start()

thread.join()

print("Finished")

class ThreadWithReturn(threading.Thread):
    def __init__(self, n, *args, **kwargs):
        super(ThreadWithReturn, self).__init__(*args, **kwargs)
        self._return = None
        self.n = n
    def run(self):
        self._return = fibonacciNum(self.n)
    def join(self):
        super(ThreadWithReturn, self).join()
        return self._return

# Start the thread and retrieve the result
thread = ThreadWithReturn(10)
thread.start()
result = thread
