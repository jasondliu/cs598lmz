import threading
# Test threading daemon

def daemon():
    print(threading.current_thread().name, 'Starting')
    time.sleep(2)
    print(threading.current_thread().name, 'Exiting')
    
def non_daemon():
    print(threading.current_thread().name, 'Starting')
    print(threading.current_thread().name, 'Exiting')
    
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# d.join()
print d.is_alive()
d.join()
print d.is_alive()

#Wait for all threads to finish
# 'd' is daemon thread, so this will not wait.
t.join()



import pytube
from pytube import YouTube

import threading

PATH = "C:\\Users\\user\\Downloads\\YouTube-Videos\\"

# Lists to store urls
