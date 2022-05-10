import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from a thread\n")).start()

def function():
  while True:
   time.sleep(0.0001)

print("Hello World!")
t1 = threading.Thread(target=function)
t1.start()

print("threads running:", threading.activeCount())
