import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        print("Goodbye")
        time.sleep(1)

