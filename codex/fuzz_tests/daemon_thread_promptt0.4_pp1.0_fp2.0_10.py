import threading
# Test threading daemon
def main():
    print('Main thread started')
    thread = threading.Thread(target=worker, args=(1,))
    thread.setDaemon(True)
    thread.start()
    print('Main thread finished')

def worker(number):
    print('Worker {} started'.format(number))
    time.sleep(3)
    print('Worker {} finished'.format(number))

main()

# Test threading non-daemon
def main():
    print('Main thread started')
    thread = threading.Thread(target=worker, args=(1,))
    thread.setDaemon(False)
    thread.start()
    print('Main thread finished')

def worker(number):
    print('Worker {} started'.format(number))
    time.sleep(3)
    print('Worker {} finished'.format(number))

main()

# Test threading lock
lock = threading.Lock()

def main():
    print('Main thread started')
    thread = threading.Thread(target=worker, args=(1,))
   
