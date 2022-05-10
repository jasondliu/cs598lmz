import sys, threading

def run():
    while True:
        print('Hello')

def main():
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        print('World')

if __name__ == '__main__':
    main()
