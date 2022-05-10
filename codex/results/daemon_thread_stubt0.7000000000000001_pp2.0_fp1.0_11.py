import sys, threading

def run():
    print("current num:", threading.activeCount())
    print("current thread:", threading.currentThread())
    time.sleep(2)

if __name__ == "__main__":
    for i in range(0,5):
        td = threading.Thread(target=run)
        td.start()
