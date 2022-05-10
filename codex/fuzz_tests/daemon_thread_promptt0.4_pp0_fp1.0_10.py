import threading
# Test threading daemon

def run():
    while True:
        print(threading.current_thread().name)
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=run,name='test_thread')
    t.setDaemon(True)
    t.start()
    print(threading.current_thread().name)
    print('main thread end')
