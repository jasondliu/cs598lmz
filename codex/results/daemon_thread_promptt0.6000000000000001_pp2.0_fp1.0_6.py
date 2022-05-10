import threading
# Test threading daemon
def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(5)
    print('Exiting :', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

def non_daemon():
    print('Starting:', threading.currentThread().name)
    print('Exiting :', threading.currentThread().name)


t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
d.join()
t.join()

print("Daemon thread is exit")
