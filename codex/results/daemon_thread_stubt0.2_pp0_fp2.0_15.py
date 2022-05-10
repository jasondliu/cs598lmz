import sys, threading

def run():
    while True:
        print('Thread {} is running'.format(threading.current_thread().name))
        time.sleep(1)

print('Thread {} is running'.format(threading.current_thread().name))
t = threading.Thread(target=run)
t.start()
t.join()
print('Thread {} ended'.format(threading.current_thread().name))
