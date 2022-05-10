import threading
# Test threading daemon

def do_this():
    global x
    while x < 300:
        x += 1

def do_after():
    global x
    while x < 600:
        x += 1

def do_this_too():
    global x
    while x < 900:
        x += 1

def main():
    global x
    x = 0
    our_thread = threading.Thread(target=do_this)
    our_thread.start()

    our_thread2 = threading.Thread(target=do_this_too)
    our_thread2.start()

    our_thread3 = threading.Thread(target=do_after)
    our_thread3.start()

    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())

if __name__ == '__main__':
    main()
