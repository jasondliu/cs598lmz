import threading
# Test threading daemon
def worker():
    print('Starting worker')
    time.sleep(0.2)
    print('Finished worker')

thread = threading.Thread(target=worker)
thread.start()
thread.join()

print('\n')

# Test threading daemon
def worker():
    print('Starting worker')
    time.sleep(0.2)
    print('Finished worker')

thread = threading.Thread(target=worker)
thread.daemon = True
thread.start()
thread.join()

print('\n')

# Test threading daemon
def worker():
    print('Starting worker')
    time.sleep(0.2)
    print('Finished worker')

thread = threading.Thread(target=worker)
thread.daemon = True
thread.start()

print('\n')

# Test threading daemon
def worker():
    print('Starting worker')
    time.sleep(0.2)
    print('Finished worker')

thread = threading.Thread(target=worker)
thread.daemon = True
