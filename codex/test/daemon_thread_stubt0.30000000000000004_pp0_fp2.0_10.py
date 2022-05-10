import sys, threading

def run():
    for i in range(100):
        print(i)
        time.sleep(0.1)

def main():
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    print("main thread")
    time.sleep(1)
    print("main thread end")

