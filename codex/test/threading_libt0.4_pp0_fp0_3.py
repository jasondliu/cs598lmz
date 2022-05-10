import threading
threading.current_thread()

def do_this():
    global x
    while x < 300:
        x += 1

def do_after():
    global x
    while x < 600:
        x += 1

def main():
    global x
    x = 0

    our_thread = threading.Thread(target=do_this, name='Our Thread')
    our_thread.start()

    our_thread = threading.Thread(target=do_after, name='Our Thread')
    our_thread.start()

if __name__ == '__main__':
    main()

#print(x)

import threading
threading.current_thread()

def do_this():
    global x
    while x < 300:
        x += 1

def do_after():
    global x
    while x < 600:
        x += 1

def main():
    global x
    x = 0

    our_thread = threading.Thread(target=do_this, name='Our Thread')
    our_thread.start()

    our_
