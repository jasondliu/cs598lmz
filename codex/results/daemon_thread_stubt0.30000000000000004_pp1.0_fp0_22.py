import sys, threading

def run():
    while True:
        print("Hello World")

def main():
    thread = threading.Thread(target=run)
    thread.start()

if __name__ == '__main__':
    main()
