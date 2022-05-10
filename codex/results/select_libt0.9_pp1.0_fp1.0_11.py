import select
import time
import grablib
from grablib import grabber
import threading

username = 'UNI'
password = 'PASSWORD'

# grab URL here
url = '<your page url. Use your own page firebase url>'

# Create Grabber
g = grablib.grabber(
    username = username,
    password = password,
    url = url
)

# Sync threads for logout, 
# Not the best way. Should use something like gevent or futures.
class Sync_Threads:
    def __init__(self):
        self.cond_var = threading.Condition()
        self.threads = []

    def acquire(self):
        self.threads.append(threading.current_thread())

    def release(self):
        self.threads.remove(threading.current_thread())
        threads = self.threads[:]
        self.cond_var.notify_all()
        return threads

    def wait(self):
        self.cond_var.acquire()
        self.cond_var.wait
