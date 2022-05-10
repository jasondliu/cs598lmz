import threading
# Test threading daemon
class TestThreading (threading.Thread):
    def __init__(self, threadID, name, server_):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.server_ = server_
        self.stop = threading.Event() #Change back 'stop' variable to stop thread.
    def run(self):
       while not self.stop.isSet(): #While stop is False, run 'loop' function
           self.loop()
    def loop(self):
        self.server_.send("test")
        if(self.stop.wait(5)): #Wait 5 seconds, if 'stop' is True, break out of loop
            break
    def stop(self):
        self.stop.set()
</code>
Apart from the non-main thread running slower than the main thread (which I don't think is a problem), I get the following error:
<code>Exception in thread Thread-1 (most likely raised during interpreter shutdown):
Traceback (most recent call last):
  File "C:\Python
