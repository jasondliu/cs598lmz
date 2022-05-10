import threading
# Test threading daemon

def do_this():
    global x
    while True:
        lock.acquire()
        while x < 300:
            x += 1
            print(x)
        lock.release()
        time.sleep(5)

def do_after():
    global x
    while True:
        lock.acquire()
        while x > 100:
            x -= 1
            print(x)
        lock.release()
        time.sleep(5)

def main():
    global x
    x = 0

    our_thread = threading.Thread(target=do_this, daemon=True)
    our_thread.start()

    our_thread2 = threading.Thread(target=do_after, daemon=True)
    our_thread2.start()

    print("Hello from main")
    time.sleep(10)
    print("Main again")

if __name__ == "__main__":
    main()
