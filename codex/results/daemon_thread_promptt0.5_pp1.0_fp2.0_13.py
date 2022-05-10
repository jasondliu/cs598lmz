import threading
# Test threading daemon
def my_thread():
    print("Hello, I'm a thread")

my_thread = threading.Thread(target=my_thread)
my_thread.daemon = True
my_thread.start()

# Test threading join
def my_thread2():
    print("Hello, I'm a thread")
    time.sleep(5)
    print("I'm done")

my_thread2 = threading.Thread(target=my_thread2)
my_thread2.start()
my_thread2.join()

print("I'm done")

# Test threading lock
def my_thread3():
    global x
    for i in range(0, 1000000):
        x += 1

def my_thread4():
    global x
    for i in range(0, 1000000):
        x -= 1

x = 0
lock = threading.Lock()
thread_1 = threading.Thread(target=my_thread3)
thread_2 = threading.Thread(target=my_thread4)
thread_1.start()
thread_2
