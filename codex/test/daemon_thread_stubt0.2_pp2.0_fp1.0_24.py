import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

def main():
    threading.Thread(target=run).start()
    while True:
        print("World")
        time.sleep(1)

