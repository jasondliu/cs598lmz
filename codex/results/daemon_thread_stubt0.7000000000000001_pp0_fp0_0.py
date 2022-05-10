import sys, threading

def run():
    print('Greetings from the child process!')
    print('The child is exiting.')

def main():
    while True:
        print('Hello from the parent process.')
        if input() == 'q': break


if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    main()
