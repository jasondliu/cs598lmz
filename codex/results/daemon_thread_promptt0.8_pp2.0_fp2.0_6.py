import threading
# Test threading daemon with a simple program

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.daemon = True
    t.start()

# 'hasattr' does not work for built-in objects. 
# Use 'getattr' instead.
while getattr(threading.current_thread(), "do_run", True):
    pass
