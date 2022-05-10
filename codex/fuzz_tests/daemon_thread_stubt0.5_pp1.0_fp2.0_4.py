import sys, threading

def run():
    for i in range(1, 100):
        print("Hello from thread %i" % i)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
