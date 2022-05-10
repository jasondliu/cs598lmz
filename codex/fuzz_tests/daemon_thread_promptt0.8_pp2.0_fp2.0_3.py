import threading
# Test threading daemon

import time

def g():
    while True:
        time.sleep(1)
        print("daemon example")


threading.Thread(target=g).start()
print("Main thread")
