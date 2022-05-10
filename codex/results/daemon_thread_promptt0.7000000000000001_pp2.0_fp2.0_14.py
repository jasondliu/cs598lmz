import threading
# Test threading daemon threads

def keyboard_thread(event):
    while True:
        raw_input()
        event.set()

def main_thread(event):
    while True:
        event.wait()
        print "You pressed Enter!"
        event.clear()

if __name__ == "__main__":
    event = threading.Event()
    keyboard_thread = threading.Thread(target=keyboard_thread, args=(event,))
    keyboard_thread.daemon = True
    keyboard_thread.start()

    main_thread(event)
