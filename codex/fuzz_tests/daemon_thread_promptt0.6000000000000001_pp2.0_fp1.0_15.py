import threading
# Test threading daemon
class MyClass(object):
    def __init__(self):
        self.count = 0

    def run(self):
        while self.count < 4:
            print "count:", self.count
            self.count += 1
            time.sleep(1)

my_obj = MyClass()
my_thread = threading.Thread(target=my_obj.run)
my_thread.daemon = True
my_thread.start()

## join() blocks until my_thread is dead
my_thread.join()

print "Done"
