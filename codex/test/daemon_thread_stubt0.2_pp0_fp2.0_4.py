import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(0.5)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        print("World")
        time.sleep(0.5)

