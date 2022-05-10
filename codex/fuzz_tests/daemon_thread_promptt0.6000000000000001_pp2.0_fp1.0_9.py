import threading
# Test threading daemon
import time

def print_time(delay):
    while True:
        print(time.ctime())
        time.sleep(delay)

t = threading.Thread(target=print_time, args=(5,))
t.daemon = True
t.start()

t.join(10)
print("Exiting")
