import threading
# Test threading daemon
def test():
    print('thread start')
    time.sleep(10)
    print('thread end')

t = threading.Thread(target=test)
t.setDaemon(True)
t.start()

# Test threading exec
def test2():
    print('thread2 start')
    time.sleep(10)
    print('thread2 end')

t2 = threading.Thread(target=test2)
t2.start()
t2.join()
