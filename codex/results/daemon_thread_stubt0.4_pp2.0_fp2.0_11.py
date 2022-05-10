import sys, threading

def run():
    while True:
        print("Thread")
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()

    while True:
        print("Main")
        time.sleep(1)
</code>

