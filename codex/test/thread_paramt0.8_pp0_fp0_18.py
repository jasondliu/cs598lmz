import sys, threading
threading.Thread(target=lambda: sys.stdout.write(threading.currentThread().name)).start()
