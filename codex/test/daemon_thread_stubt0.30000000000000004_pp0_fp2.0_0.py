import sys, threading

def run():
    while True:
        print("hello world")

def main():
    t = threading.Thread(target=run)
    t.start()
    while True:
        print("hello world")

if __name__ == '__main__':
    main()
