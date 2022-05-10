import threading
# Test threading daemon
# https://stackoverflow.com/questions/190010/daemon-threads-explanation

import time

def do_work(start):
    
    time.sleep(3)
    print("Work {} done".format(start))

for i in range(5):
    t = threading.Thread(target=do_work, args=(i,))
    t.setDaemon(True)
    t.start()

print("A")

print("B")

print("C")

time.sleep(15)
