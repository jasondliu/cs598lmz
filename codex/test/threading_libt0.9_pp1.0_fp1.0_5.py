import threading
threading.stack_size(2**26)

def BackgroundWorker(task):
    import time, sys
    while True:
        time.sleep(0.0002)
