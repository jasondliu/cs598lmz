import threading
# Test threading daemon mode:

def d():
    for x in range(5):
        print threading.current_thread().name, x

t = threading.Thread(target=d, name="daemon")
t.daemon = True
t.start()

#t.join()
