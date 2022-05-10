import sys, threading

def run():
    while True:
        time.sleep(1)

def main():
    threading.Thread(target=run).start()
    while True:
        pass

if __name__ == '__main__':
    main()
