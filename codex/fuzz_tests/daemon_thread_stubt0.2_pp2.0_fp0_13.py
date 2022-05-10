import sys, threading

def run():
    while True:
        print("hello")

def main():
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()

if __name__ == '__main__':
    main()
