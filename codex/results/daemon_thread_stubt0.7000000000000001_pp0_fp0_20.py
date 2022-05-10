import sys, threading

def run():
    while True:
        q.put(".")

def run2():
    while True:
        q.put("$")

q = Queue()

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

thread2 = threading.Thread(target=run2)
thread2.daemon = True
thread2.start()

while True:
    sys.stdout.write(q.get())
