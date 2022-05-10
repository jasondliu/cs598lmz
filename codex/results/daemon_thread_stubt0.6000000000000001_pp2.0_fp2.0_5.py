import sys, threading

def run():
    while True:
        print("threading")
        time.sleep(100)

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    print("main threading")
    time.sleep(1000)
