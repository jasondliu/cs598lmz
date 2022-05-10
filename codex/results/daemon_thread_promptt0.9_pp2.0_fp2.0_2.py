import threading
# Test threading daemon function
def worker():
    name = threading.currentThread().getName()
    print(name, 'Starting')
    time.sleep(2)
    print(name, 'Exiting')
def my_service():
    name = threading.currentThread().getName()
    print(name, 'Starting')
    time.sleep(3)
    print(name, 'Exiting')
t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)     # use default name
w.start()
w2.start()
t.start()
# set threads daemon
print("Now set them all daemon\n")
t.setDaemon(True)
w.setDaemon(True)
w2.setDaemon(True)
# test join function
t.join()
print("T.join done\n")
w.join()
print("W.join done\n")
# test threading enumerate function
print("Enumerate done")
