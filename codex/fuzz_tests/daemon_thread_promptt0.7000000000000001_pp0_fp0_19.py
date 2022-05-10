import threading
# Test threading daemonic mode

def worker():
    print("worker")
    time.sleep(1)
    print("worker")

t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()
print("main")

time.sleep(0.5)
print("main")

time.sleep(0.5)
print("main")

time.sleep(0.5)
print("main")

time.sleep(0.5)
print("main")

time.sleep(0.5)
print("main")

time.sleep(0.5)
print("main")


time.sleep(0.5)
print("main")

time.sleep(0.5)
print("main")


time.sleep(0.5)
print("main")

time.sleep(0.5)
print("main")

time.sleep(0.5)
print("main")


time.sleep(0.5)
print("main")

time.sleep(0.5)
print("main")


