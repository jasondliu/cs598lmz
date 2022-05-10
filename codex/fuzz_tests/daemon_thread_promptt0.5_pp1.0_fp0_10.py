import threading
# Test threading daemon

def test_thread():
    while True:
        print('test_thread')
        time.sleep(1)

t = threading.Thread(target=test_thread, daemon=True)
t.start()

while True:
    print('main thread')
    time.sleep(1)

# Test threading non daemon

def test_thread():
    while True:
        print('test_thread')
        time.sleep(1)

t = threading.Thread(target=test_thread, daemon=False)
t.start()

while True:
    print('main thread')
    time.sleep(1)

# Test multiprocessing daemon

def test_process():
    while True:
        print('test_process')
        time.sleep(1)

p = multiprocessing.Process(target=test_process)
p.daemon = True
p.start()

while True:
    print('main process')
    time.sleep(1)

# Test multiprocessing non daemon

def test_process():

