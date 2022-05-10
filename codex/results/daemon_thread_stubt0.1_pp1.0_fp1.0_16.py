import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    print("Hello from main")
    time.sleep(5)
    print("Bye from main")
    sys.exit()
</code>

