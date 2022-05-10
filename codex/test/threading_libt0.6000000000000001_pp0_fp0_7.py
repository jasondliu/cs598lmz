import threading
threading.stack_size(2048*2048)

class Test(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stopit = threading.Event()
        self.stopit.clear()
