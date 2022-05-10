import threading
# Test threading daemon type
def timer():
    print(time.ctime(),'Timer expires')

t = threading.Timer(3,timer)
t.setDaemon(True)
t.start()

print(f"Daemon status:{t.isDaemon()}")
print(f"Active threads:{threading.active_count()}")
