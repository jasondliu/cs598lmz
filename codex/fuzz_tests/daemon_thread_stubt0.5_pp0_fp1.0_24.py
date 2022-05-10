import sys, threading

def run():
    while True:
        print('Hello from thread')
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.setDaemon(True)
    thread.start()
    while True:
        print('Hello from main')
        time.sleep(1)

if __name__ == '__main__':
    main()
</code>

