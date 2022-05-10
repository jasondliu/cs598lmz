import sys, threading
threading.Thread(target=lambda:sys.__stdout__.write(input(''))).start()
