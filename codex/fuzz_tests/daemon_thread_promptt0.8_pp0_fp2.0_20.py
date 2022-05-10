import threading
# Test threading daemon

t1 = threading.Thread(target=print, args=("test",))
t1.setDaemon(True)
t1.start()

t1.join()

input("END")   # press any key to exit
