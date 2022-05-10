import threading
# Test threading daemon

def daemon():
    print('Starting:')
    time.sleep(2)
    print('Exiting')

def non_daemon():
    print('Starting:')
    print('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print('d.isAlive()', d.isAlive())
print('t.isAlive()', t.isAlive())

print('d.name', d.name)
print('t.name', t.name)

print('d.ident', d.ident)
print('t.ident', t.ident)

print('d.daemon', d.daemon)
print('t.daemon', t.daemon)

print('d.is_alive()', d.is_alive())
print('t.is_alive
