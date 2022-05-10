import threading
# Test threading daemon
def test(number):
    while True:
        print('test', number)
        time.sleep(0.5)

t1 = threading.Thread(target=test, args=(1,))
t1.daemon = True
t1.start()

t2 = threading.Thread(target=test, args=(2,))
t2.daemon = True
t2.start()

print('main thread')
