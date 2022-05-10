import threading
# Test threading daemon
def threading_daemon(name):
    while True:
        print("Threading daemon: " + name)
        time.sleep(3)

threading_1 = threading.Thread(target=threading_daemon, args=("threading_1",))
threading_2 = threading.Thread(target=threading_daemon, args=("threading_2",))
threading_1.setDaemon(True)
threading_2.setDaemon(True)
threading_1.start()
threading_2.start()

while True:
    print("Main threading")
    time.sleep(3)

# Test threading daemon
def threading_daemon(name):
    while True:
        print("Threading daemon: " + name)
        time.sleep(3)

threading_1 = threading.Thread(target=threading_daemon, args=("threading_1",))
threading_2 = threading.Thread(target=threading_daemon, args=("threading_2",))
threading_
