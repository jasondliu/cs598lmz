import threading
# Test threading daemon
def myThread():
    for i in range(5):
        print("thread")
        time.sleep(1)

t = threading.Thread(target=myThread)
t.setDaemon(True)
t.start()
time.sleep(1)
