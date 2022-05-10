import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 3\n')).start()

# or just
from threading import Thread
Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

# The threading module is also great for distributing work across multiple cores,
# even if the work is something as simple as downloading web pages.
from threading import Thread
from time import time
from urllib.request import urlopen

# a function that takes a URL, downloads the page and measures how long it took
def download(url):
    resp = urlopen(url)
    print('Read {} from {}'.format(len(resp.read()), url))

# Create an empty list to store our threads
threads = []
# Create 10 threads that run the download function with different URLs
for i in range(10):
    t = Thread
