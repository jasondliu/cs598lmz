import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html#threading.Thread.daemon

def worker():
    """thread worker function"""
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

print(threading.current_thread().getName())
print(threading.current_thread().is_alive())
print(threading.current_thread().isDaemon())
print(threading.current_thread().ident)
print(threading.current_thread().name)
print(threading.current_thread().daemon)
print(threading.current_thread().is_alive())
print(threading.current_thread().isDaemon())
print(threading.current_thread().ident)
print(threading.current_thread().name)
print(threading.current_thread().daemon)

# print(threading.current_thread().is_alive())
# print(
