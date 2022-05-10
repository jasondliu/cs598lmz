import sys, threading

def run():
    while True:
        print("Hello World")
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    while True:
        time.sleep(2)
        print("Goodbye World")
</code>

