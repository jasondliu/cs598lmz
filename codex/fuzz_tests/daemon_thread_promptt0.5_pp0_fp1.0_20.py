import threading
# Test threading daemon

def daemon():
    print('Starting:')
    time.sleep(2)
    print('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:')
    print('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# d.join()
# t.join()

print(d.isAlive())
print(t.isAlive())

print(d.isDaemon())
print(t.isDaemon())

# d.setDaemon(False)
# print(d.isDaemon())

# t.setDaemon(True)
# print(t.isDaemon())

# t.setDaemon(False)
# print(t.isDaemon())

# d.setDaemon(True)
# print(d.isDaemon())

# d.setDaemon(False
