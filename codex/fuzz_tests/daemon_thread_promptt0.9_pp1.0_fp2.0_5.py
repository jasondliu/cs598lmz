import threading
# Test threading daemon.
import time

def callback():
    global x
    x = 1
    print("callback")

def main(callback):
    print("main 1")
    t = threading.Thread(target=callback)
    t.setDaemon(True)
    t.start()
    print("main 2")
    print("main 3")
    time.sleep(3)
    print("main 4")
    print(x)


x = 0
main(callback)

print("Done.")
