import sys, threading

def run():
    for i in range(0, 5):
        print('Thread 1')

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()

    for i in range(0, 5):
        print('Thread 2')
