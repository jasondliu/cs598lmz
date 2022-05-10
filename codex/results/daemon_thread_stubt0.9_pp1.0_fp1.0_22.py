import sys, threading

def run():
    event.wait()
    print(r)

event = threading.Event()
r = 0

thread = threading.Thread(target=run)
thread.start()

for i in range(10):
    r += 1
time.sleep(1)
event.set()
thread.join()
print(r)
