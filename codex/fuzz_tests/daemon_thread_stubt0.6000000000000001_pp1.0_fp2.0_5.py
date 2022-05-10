import sys, threading

def run():
    for i in range(10):
        print(i)

def main():
    thread = threading.Thread(target=run)
    thread.start()

if __name__ == '__main__':
    main()
