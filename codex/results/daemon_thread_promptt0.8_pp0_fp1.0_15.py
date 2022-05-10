import threading
# Test threading daemon
def do_something():
    print('start')
    time.sleep(5)
    print('end')

t = threading.Thread(target=do_something)
t.setDaemon(True)
t.start()

t2 = threading.Thread(target=do_something)
t2.setDaemon(True)
t2.start()

t.join()

print('Main thread end')
