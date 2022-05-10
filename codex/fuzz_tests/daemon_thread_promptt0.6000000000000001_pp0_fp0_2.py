import threading
# Test threading daemon mode
def target():
    print('Thread started')
    time.sleep(1)
    print('Thread ended')
    
thread = threading.Thread(target=target)
thread.start()
thread.join()

print('Thread done')
# Test threading daemon mode
def target():
    print('Thread started')
    time.sleep(1)
    print('Thread ended')
    
thread = threading.Thread(target=target)
thread.daemon = True
thread.start()
thread.join()

print('Thread done')
 
# Test threading
threads = []
for _ in range(10):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()

print('Thread done')
 
# Test threading
threads = []
for i in range(10):
    thread = threading.Thread(target=target, args=(i,))
    thread.daemon = True
    thread.start
