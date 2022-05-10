import threading
# Test threading daemonic
def daemon():
    print('Start daemon')
    time.sleep(2)
    print('Stop daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start non-daemon')
    print('Stop non-daemon')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading
def doubler(number):
    """
    A function that can be used by a thread
    """
    print(f'{threading.currentThread().getName()}')
    print(f'{threading.currentThread().ident}')
    print(f'{threading.enumerate()}')
    result = number * 2
    print(f'{threading.currentThread().name} doubled to {result}')

if __name__ == '__main__':
    for i in range(5):
        my_thread = threading.Thread
