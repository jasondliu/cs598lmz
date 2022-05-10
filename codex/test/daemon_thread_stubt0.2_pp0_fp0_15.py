import sys, threading

def run():
    while True:
        print("Hello from a thread!")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        print("Hello from the main thread!")
        time.sleep(1)

