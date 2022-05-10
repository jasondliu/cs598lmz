import threading
# Test threading daemon

def daemon():
    print('daemon start')
    time.sleep(10)
    print('daemon end')
d = threading.Thread(target=daemon)
d.setDaemon(True)
d.start()

print('non-daemon start')
time.sleep(3)
print('non-daemon end')

import threading
# Test threading join

def daemon():
    print('daemon start')
    time.sleep(10)
    print('daemon end')
d = threading.Thread(target=daemon)
d.setDaemon(True)
d.start()

print('non-daemon start')
d.join()
print('non-daemon end')

import threading
# Test threading join

def daemon():
    print('daemon start')
    time.sleep(10)
    print('daemon end')
d = threading.Thread(target=daemon)
d.setDaemon(True)
d.start()

print('non-daemon start')
d.join(3
