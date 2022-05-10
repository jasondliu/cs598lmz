import sys, threading

def run():
    while True:
        print('thread running')
        time.sleep(0.5)

def main():
    t = threading.Thread(target=run)
    t.start()
    while True:
        print('main thread running')
        time.sleep(0.5)

if __name__ == '__main__':
    main()
