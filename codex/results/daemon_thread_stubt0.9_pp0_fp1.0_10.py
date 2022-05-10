import sys, threading

def run():
    for x in range(100):
        print (x)
        time.sleep(0.01)
 
 
 
for i in range(1000):
    t = threading.Thread(target=run)
    t.start()
</code>

