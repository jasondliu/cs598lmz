import threading
# Test threading daemon
def work():
    print('thread start')
    time.sleep(3)
    print('thread end')

t = threading.Thread(target=work)
t.setDaemon(True)
t.start()
print('main thread start')
t.join()
print('main thread end')
