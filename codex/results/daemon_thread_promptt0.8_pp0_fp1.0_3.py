import threading
# Test threading daemon vs non-daemon

def threading_test(number, daem):
    t = threading.Thread(target=worker, name="thread-"+str(number), args=(number,))
    t.setDaemon(daem)
    print("Starting ", t.name)
    t.start()
    print("exiting ", t.name)


def worker(number):
    print("Worker ", number, " Started")
    time.sleep(2)
    print("Worker ", number, " Finished")

for i in range(10):
    threading_test(i, True)

print("Main Thread Finished!")



# Test object attributes vs local vars

class Worker:
    def __init__(self, val):
        self.val = val
        print("I am alive!")
    
    def proccess(self):
        print(self.val)

w = Worker(10)
w.proccess()

def test_vars():
    val = 20
    print(val)

test_vars()


# Test
