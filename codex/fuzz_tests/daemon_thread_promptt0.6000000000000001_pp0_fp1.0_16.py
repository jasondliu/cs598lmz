import threading
# Test threading daemon
def my_thread():
    print('Hello from a thread!')
    time.sleep(5)
    print('Bye')

if __name__ == '__main__':
    t = threading.Thread(target=my_thread)
    t.daemon = True
    t.start()
    print('Hello from main thread')
    time.sleep(3)
    print('Bye from main thread')
