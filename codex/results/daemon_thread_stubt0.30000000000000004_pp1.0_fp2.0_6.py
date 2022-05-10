import sys, threading

def run():
    while True:
        print("Hello")

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()

    while True:
        print("World")
