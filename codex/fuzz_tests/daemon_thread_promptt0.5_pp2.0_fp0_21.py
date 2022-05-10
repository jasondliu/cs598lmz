import threading
# Test threading daemon

def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)

def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print('d.isAlive()', d.isAlive())
print('t.isAlive()', t.isAlive())

print('Exiting Main Thread')

# The main thread exits when all non-daemon threads exit

# Output:
# Starting: daemon
# Starting: non-daemon
# Exiting : non-daemon
# Exiting : daemon
# d.isAlive() False
#
