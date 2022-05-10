import threading
# Test threading daemon.
thread = threading.Thread(target=lambda: print('Hello'))
thread.setDaemon(True)
thread.start()

# Force thread to end now.
threading.currentThread().join()

print('Ended')
 
# With threading locking.
lock = threading.Lock()
thread = threading.Thread(target=lambda: lock.acquire())
thread.setDaemon(True)
thread.start()
threading.currentThread().join()
print('Ended')

# With threading locking daemon.
lock = threading.Lock()
thread = threading.Thread(target=lambda: lock.acquire())


thread.start()
print('Not Ended')
