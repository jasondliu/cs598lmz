import threading
# Test threading daemon
import time

def do_this():
    global x
    while True:
        time.sleep(1)
        print("Doing this!")
        x += 1

def do_after():
    global x
    while True:
        print("Doing that!")
        time.sleep(1)
        x -= 1

def main():
    global x
    x = 0
    our_thread = threading.Thread(target=do_this, daemon=True)
    our_thread.start()
    print("Hello from main")
    time.sleep(5)
    print("Goodbye from main")

if __name__ == "__main__":
    main()

# Test threading non-daemon
import threading
# Test threading daemon
import time

def do_this():
    global x
    while True:
        time.sleep(1)
        print("Doing this!")
        x += 1

def do_after():
    global x
    while True:
        print("Doing that!")
        time.sleep(1
