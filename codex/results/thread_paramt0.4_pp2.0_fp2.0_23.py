import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello from thread\n")).start()

from time import sleep
sleep(1)

print("hello from main")

from time import sleep
sleep(1)

print("goodbye from main")
