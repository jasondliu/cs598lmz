import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

d = threading.Thread(name='daemon',target=test_daemon)
d.setDaemon(True)

def non_daemon():
    print('start')
    print('end')

t = threading.Thread(name='non-daemon',target=non_daemon)

d.start()
t.start()
d.join()
t.join()
