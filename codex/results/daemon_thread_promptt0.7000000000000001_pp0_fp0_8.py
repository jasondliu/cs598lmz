import threading
# Test threading daemon
print('Name:', threading.current_thread().getName())
print('Daemon:', threading.current_thread().isDaemon())

t = threading.Thread(target=countdown, name='CountdownThread', args=(10,), daemon=True)
t.start()

def countdown(n):
    while n > 0:
        n -= 1
        
class CountdownTask:
    def __init__(self):
        self._running = True
        
    def terminate(self):
        self._running = False
        
    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)
            
c = CountdownTask()
t = threading.Thread(target=c.run, args=(10,))
t.start()

c.terminate()
t.join()
# Threading example
from threading import Thread
from socket import AF_INET, socket, SOCK_STREAM
from time import sleep


class Client(Thread):
   
