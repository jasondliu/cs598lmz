import threading
# Test threading daemon!

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True #setting the thread running to true
 
    def run(self):
        while self.running:
            print "my thread2 uptime = %f, load_avg = %f" % (float(os.popen('cat /proc/uptime | cut -d " " -f 1').readline()), float(os.popen("cat /proc/loadavg | cut -d \" \" -f 1").readline()))
            time.sleep(1)
 
    def stop(self):
        self.running = False

t = MyThread()
t.daemon = True
t.start()

start = time.time()
while True:
    print "my thread1 uptime = %f, load_avg = %f" % (float(os.popen('cat /proc/uptime | cut -d " " -f 1').readline()), float(os.popen("cat /
