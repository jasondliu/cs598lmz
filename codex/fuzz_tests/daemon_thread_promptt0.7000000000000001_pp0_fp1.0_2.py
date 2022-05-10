import threading
# Test threading daemon
def write_data():
    while True:
        print 'Write data'
        time.sleep(2)

thread = threading.Thread(target=write_data, daemon=True)
thread.start()
# Test threading
def write_data():
    while True:
        print 'Write data'
        time.sleep(2)

def read_data():
    while True:
        print 'Read data'
        time.sleep(2)

thread = threading.Thread(target=write_data)
thread.start()
# Test threading
def write_data():
    while True:
        print 'Write data'
        time.sleep(2)

def read_data():
    while True:
        print 'Read data'
        time.sleep(2)

thread1 = threading.Thread(target=write_data)
thread1.start()
thread2 = threading.Thread(target=read_data)
thread2.start()
# Test threading 2
def write_data(t):
    while True:
        print 'Thread', t,
