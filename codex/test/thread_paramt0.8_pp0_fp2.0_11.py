import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b]2;this is the window title\x07")).start()

q = queue.Queue()

def first():
    for i in range(20):
        time.sleep(1)
        q.put("first " + str(i))

def second():
    for i in range(20):
        time.sleep(1)
        q.put("second " + str(i))

def log():
    for i in range(20):
        print(q.get())

threading.Thread(target=first, daemon = True).start()
threading.Thread(target=second, daemon = True).start()
threading.Thread(target=log, daemon = True).start()
