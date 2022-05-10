import sys, threading

def run():
    for i in range(1, 10):
        print('threading')

def main():
    for i in range(1, 10):
        print('main')

if __name__ == '__main__':
    thread = threading.Thread(target=run)
    thread.start()
    main()
