import threading
# Test threading daemon.

class MyThread(threading.Thread):
    result = ''

    def __init__(self, **kwargs):
        super(MyThread, self).__init__()
        self.function = kwargs.get('function')
        self.args = kwargs.get('args')
        self.kwargs = kwargs.get('kwargs')
        self.result = ''
        
    def run(self):
        self.result = self.function(*self.args, **self.kwargs)
        return self.result

    def start(self):
        threading.Thread.start(self)

# This launches the thread depending on what function is received. 
# def startThread(function, args = (), kwargs = {}):
#     global exec_thread
#     exec_thread = MyThread(function = function, args = args, kwargs = kwargs)
#     exec_thread.setDaemon(True)
#     exec_thread.start()
#     return exec_thread

def startThread(function, args = (), kwargs =
