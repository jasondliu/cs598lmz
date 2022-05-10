import sys, threading

def run():
    for i in range(100):
        print(i)

def main():
    thread = threading.Thread(target=run)
    thread.start()

    while True:
        print('Main')

if __name__ == '__main__':
    main()
