import threading
# Test threading daemon
def dosomething():
    print ("work thread is running")
    x=0
    while True:
        x=x^1
        print ("x=",x)
        time.sleep(1)
#main thread
print ("main thread is running")
d=threading.Thread(target=dosomething)
d.setDaemon(True)
d.start()
#time.sleep(3)
#print ("main thread is ending")

print ("main thread is ended")
