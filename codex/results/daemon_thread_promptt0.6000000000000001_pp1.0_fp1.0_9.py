import threading
# Test threading daemon

def sayhi():
    print("hello world")
    time.sleep(3)
    print("goodbye")

for i in range(5):
    t = threading.Thread(target=sayhi)
    t.setDaemon(True)
    t.start()

print("main thread")
