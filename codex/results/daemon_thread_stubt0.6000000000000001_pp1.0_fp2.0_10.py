import sys, threading

def run():
    while True:
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()

    while True:
        time.sleep(1)
</code>

