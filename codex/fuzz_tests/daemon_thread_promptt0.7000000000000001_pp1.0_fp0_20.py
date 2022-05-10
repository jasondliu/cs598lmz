import threading
# Test threading daemon to run a function in the background

def do_something():
    print("Thread started")
    while True:
        print("Doing something")
        time.sleep(2)

t = threading.Thread(target=do_something)
t.daemon = True
t.start()

print("Thread finished")
    

# Test threading daemon to run a function in the background

def do_something():
    print("Thread started")
    while True:
        print("Doing something")
        time.sleep(2)

t = threading.Thread(target=do_something)
t.daemon = True
t.start()

print("Thread finished")

# Test threading daemon to run a function in the background

def do_something():
    print("Thread started")
    while True:
        print("Doing something")
        time.sleep(2)

t = threading.Thread(target=do_something)
t.daemon = True
t.start()

print("Thread finished")
 
# Test threading daemon to run a function
