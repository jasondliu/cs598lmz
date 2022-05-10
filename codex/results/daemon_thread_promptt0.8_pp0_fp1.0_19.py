import threading
# Test threading daemon

class TestTh(threading.Thread):
    def run(self):
        while True:
            print("Test Thread")
            time.sleep(1)
        
    def stop(self):
        pass
    
    
def run():
    th = TestTh()
    th.start()
    
def stop():
    pass
    
# Server

# Test threading non-daemon
class TestTh(threading.Thread):
    def run(self):
        while True:
            print("Test Thread")
            time.sleep(1)
    

def run():
    th = TestTh()
    th.start()
    
def stop():
    pass

 
# Server.py
if __name__ == '__main__':
    try:
        server = ThreadingSimpleServer(('', 9090), Handler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")
        server.shutdown()


# Test Threads
import threading
import time

class TestTh(threading.Thread):
   
