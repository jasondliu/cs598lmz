import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

if __name__ == '__main__':
    thread = threading.Thread(target=run)
    thread.start()
    for i in range(10):
        print("World")
        time.sleep(1)
