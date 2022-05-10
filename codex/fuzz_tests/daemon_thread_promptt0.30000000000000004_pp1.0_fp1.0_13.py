import threading
# Test threading daemon

def worker():
    print('worker')
    time.sleep(1)
    print('worker')

t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()

print('main')

# main
# worker
# worker

# main thread exit, daemon thread exit

# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
# worker
# main
# worker
