import threading
# Test threading daemon
def thread_run():
    while True:
        print("Hello World!")
        time.sleep(2)

thread = threading.Thread(target = thread_run)
thread.daemon = True
thread.start()

print("Hello main")
time.sleep(10)
print("Bye main")

# Test threading not daemon
def thread_run():
    while True:
        print("Hello World!")
        time.sleep(2)

thread = threading.Thread(target = thread_run)
thread.daemon = False
thread.start()

print("Hello main")
time.sleep(10)
print("Bye main")
