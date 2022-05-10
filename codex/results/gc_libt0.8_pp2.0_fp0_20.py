import gc, weakref, time

class MemTest:
    def __init__(self, *args, **kwargs):
        print "Initializing a MemTest object..."
        self.a = 10
        self.b = "some text"
        self.c = [1, 2, 3, 4]
        self.d = {'key': 'value', 'key2': 'value2'}
        self.e = (1, 2, 3, 4)
        self.f = {1, 2, 3, 4}
        self.g = long(0x10101010)
        print "Finished initializing"
        

class MemoryWatch():
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):
        print "Memory watch started..."
        self.start_mem = psutil.virtual_memory().used
        self.start_time = time.clock()
        return self

    def __exit__(self, *args):
        self.end_mem = psutil.virtual_memory().used
        self.end_time =
