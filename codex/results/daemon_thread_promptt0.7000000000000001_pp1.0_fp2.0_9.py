import threading
# Test threading daemon
print("\n" + "*" * 50 + "\n" + "Test threading daemon\n" + "*" * 50 + "\n")
def f():
    i = 0
    while True:
        print("It's me " + str(i))
        i += 1
        time.sleep(1)

t = threading.Thread(target=f)
t.daemon = True
t.start()
time.sleep(5)
print("End")

# Test runnable
print("\n" + "*" * 50 + "\n" + "Test runnable\n" + "*" * 50 + "\n")
class MyThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter

    def run(self):
        print("Start thread " + self.name)
        print_time(self.name, self.counter, 5)
        print("End thread " + self.name)

def print_
