import threading
# Test threading daemon functionality

def loop():
    threading.current_thread().name = 'Loop'
    for i in range(5):
        print('Thread {} is running...'.format(threading.current_thread().name))
        time.sleep(0.5)


print('Thread {} is running...'.format(threading.current_thread().name))
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()

print('Thread {} ended.'.format(threading.current_thread().name))
