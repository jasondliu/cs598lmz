import sys, threading

def run():
    for i in range(1000):
        print("child: hello")
        sleep(0.1)

# thread
t = threading.Thread(target=run)
t.start()
# main thread
while True:
    print("parent: hello")
    sleep(1.0)
