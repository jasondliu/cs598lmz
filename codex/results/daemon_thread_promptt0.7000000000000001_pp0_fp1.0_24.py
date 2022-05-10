import threading
# Test threading daemonic
def loop():
    while True:
        print('thread %s is running...' % threading.current_thread().name)
        time.sleep(1)
    print('thread %s is end.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s is end.' % threading.current_thread().name)
