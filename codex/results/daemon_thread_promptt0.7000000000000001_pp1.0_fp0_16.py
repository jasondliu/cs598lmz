import threading
# Test threading daemon

def output(num):
    for i in range(num):
        print("The number is {}.".format(i))
        time.sleep(1)

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.daemon = True
        self.num = num

    def run(self):
        output(self.num)

t = MyThread(10)
t.start()
print("Waiting for thread.\n")
t.join()

print("All done.")
