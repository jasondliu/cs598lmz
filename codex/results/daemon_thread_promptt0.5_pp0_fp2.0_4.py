import threading
# Test threading daemon
# https://stackoverflow.com/questions/6920302/making-a-daemon-thread-in-python

class MyThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            print("Doing something important in a thread")
            time.sleep(1)

MyThread()
print("Doing something important in the main thread")
time.sleep(5)
print("Main thread finishing")

# https://stackoverflow.com/questions/6920302/making-a-daemon-thread-in-python

# Test asyncio
# https://stackoverflow.com/questions/17126857/how-to-call-asyncio-async-method-from-a-thread

import asyncio
import threading

async def test(name):
    print("Hello", name)

def thread
