import threading
# Test threading daemon
import time
import random
import sys

class MyThread(threading.Thread):
    def run(self):
        pause = random.randint(1, 5)
        print(f'{self.name} sleeping for {pause} sec')
        time.sleep(pause)
        print(f'{self.name} exiting')

for i in range(3):
    t = MyThread()
    t.setDaemon(True)
    t.start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    print(f"Joining {t.getName()}")
    t.join()
