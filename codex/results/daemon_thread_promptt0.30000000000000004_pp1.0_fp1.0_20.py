import threading
# Test threading daemon
# https://stackoverflow.com/questions/190010/daemon-threads-explanation

def f():
    print('thread function')
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        print(t.getName())
        t.join()

# thread function
# Thread-1
# Thread-2
# Thread-3
# thread function
# thread function
# thread function
# Thread-4
# Thread-5
# Thread-6
# thread function
# thread function
# thread function
# Thread-7
# Thread-8
# Thread-9
# thread function
# thread function
# thread function
# Thread-10
# Thread-11
# Thread-12
# thread function
# thread function
# thread function
#
