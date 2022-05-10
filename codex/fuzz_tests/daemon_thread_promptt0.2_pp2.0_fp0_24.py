import threading
# Test threading daemon
def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading join
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
t = threading.Thread(target=c.run, args=(
