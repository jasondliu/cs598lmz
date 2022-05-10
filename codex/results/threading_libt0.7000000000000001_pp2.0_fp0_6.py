import threading
threading.stack_size(64000000)


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        while True:
            print "Starting thread ", self.num
            time.sleep(1)


for i in range(1000):
    MyThread(i).start()
</code>
The script is supposed to create 1000 threads, print a line and sleep for 1 second.
However it only creates a few threads and the script terminates after a few seconds.
Any ideas why?


A:

This is because of the GIL. Python's Global Interpreter Lock doesn't actually allow true threading. So you are actually running only one thread at a time.

