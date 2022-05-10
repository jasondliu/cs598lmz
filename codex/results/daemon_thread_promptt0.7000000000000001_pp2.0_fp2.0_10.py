import threading
# Test threading daemon
def daemon():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print(threading.currentThread().getName(), 'Starting')
    print(threading.currentThread().getName(), 'Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

t.start()
d.start()

#t.join()

# Test ThreadPoolExecutor
def foo(a, b=10):
    print('running foo', a, b)

with futures.ThreadPoolExecutor(max_workers=3) as executor:
    future_result = {executor.submit(foo, i, i+1): i for i in range(5)}
    print(future_result)
    for future in futures.as_completed(future_result):
