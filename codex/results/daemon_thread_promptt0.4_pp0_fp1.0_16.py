import threading
# Test threading daemon

def do_this():
    global x

    while True:
        lock.acquire()
        print(x)
        x += 1
        lock.release()
        time.sleep(1)

def do_after():
    global x

    while True:
        lock.acquire()
        print(x)
        x += 1
        lock.release()
        time.sleep(1)

def main():
    global x, lock

    x = 0
    lock = threading.Lock()

    our_thread = threading.Thread(target=do_this, daemon=True)
    our_thread.start()

    print("Hello from main")
    time.sleep(5)
    print("Main again")

    do_after()

if __name__ == "__main__":
    main()
