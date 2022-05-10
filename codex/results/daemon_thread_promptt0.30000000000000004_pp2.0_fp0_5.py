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

x = 0

our_thread = threading.Thread(target=do_this)
our_thread.start()

our_thread = threading.Thread(target=do_after)
our_thread.start()

our_thread = threading.Thread(target=do_this_too)
our_thread.start()

print(x)

# Test threading daemon

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

x = 0

our_thread = threading.Thread
