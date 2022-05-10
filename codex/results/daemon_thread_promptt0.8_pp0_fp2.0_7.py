import threading
# Test threading daemon
import time
from time import sleep

def read(**kwargs):
    global counter
    counter = 0
    while True:
        sleep(1)
        print("\n" * 100)
        print("COUNTER: " + str(counter))
        counter += 1


def main():
    readThread = threading.Thread(name="readThread", target=read, daemon=True)
    readThread.start()
    while True:
        sleep(10)

if __name__ == "__main__":
    main()
