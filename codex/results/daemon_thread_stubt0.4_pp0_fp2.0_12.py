import sys, threading

def run():
    while True:
        print("thread")
        time.sleep(1)

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    while True:
        print("main")
        time.sleep(1)
</code>

