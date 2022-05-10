import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    while True:
        time.sleep(1)
        print("World")
</code>

