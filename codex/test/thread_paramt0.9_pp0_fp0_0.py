import sys, threading
threading.Thread(target=lambda:sys.modules[__name__].__file__).start()
