import threading
# Test threading daemon
def do_this():
    global x
    while True:
        x = x + 1
        print(x)
        time.sleep(1)

def do_after():
    global x
    while True:
        x = x + 1
        print(x)
        time.sleep(1)

def main():
    global x
    x = 0

    our_thread = threading.Thread(target=do_this, daemon=True)
    our_thread.start()

    our_thread2 = threading.Thread(target=do_after)
    our_thread2.start()

    print('Hello I am main')
    time.sleep(5)
    print('I am main again')

if __name__ == '__main__':
    main()

# Test threading lock
def do_this():
    global x
    while True:
        lock.acquire()
        x = x + 1
        print(x)
        lock.release()
        time.sleep(1)

def do_after():
    global x
    while True
