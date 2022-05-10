import sys, threading

def run():
    while True:
        command = input()
        if command == 'exit':
            break
        elif command == 'test':
            print('test')

def main():
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
