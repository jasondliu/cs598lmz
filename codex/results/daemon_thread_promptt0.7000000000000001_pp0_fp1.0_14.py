import threading
# Test threading daemon
def daemonThreadFunc():
    while True:
        print("Hello World")
        time.sleep(1)

t = threading.Thread(target=daemonThreadFunc)
t.setDaemon(True)
t.start()

while True:
    pass
