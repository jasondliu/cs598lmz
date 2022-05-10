import threading
# Test threading daemon
def daemon():
    print('Start')
    time.sleep(2)
    print('End')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
d.start()
d.join()

# Test threading non-daemon
def non_daemon():
    print('Start')
    time.sleep(2)
    print('End')

d = threading.Thread(name='non-daemon', target=non_daemon)
d.start()
d.join()

# Test threading with args
def with_args(num1, num2):
    print(num1 + num2)

d = threading.Thread(name='with_args', target=with_args, args=(1,2))
d.start()
d.join()
