import threading
threading.stack_size(2048*2048)

class Test(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stopit = threading.Event()
        self.stopit.clear()
    def run(self):
        print "I am a thread"
        print "I am going to sleep"
        time.sleep(5)
        print "I am awake now"
        self.stopit.set()
    def stop(self):
        self.stopit.set()

t = Test()
t.start()
t.join()
print "I am not a thread"
</code>
This produces the following output:
<code>I am a thread
I am going to sleep
I am awake now
I am not a thread
</code>

