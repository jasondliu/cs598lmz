import threading
# Test threading daemon 
import time

def daemon():
    print('Starting:')
    time.sleep(0.2)
    print('Exiting:')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:')
    print('Exiting:')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
# d.join()
t.join()

# print(d.is_alive())
# print(t.is_alive())
# print(d.daemon)
# print(t.daemon)

# print(d.name)
# print(t.name)

# print(d.ident)
# print(t.ident)

# print(d.getName())
# print(t.getName())

# print(d.is_alive())
# print(t.is_alive())

# print(d.isDa
