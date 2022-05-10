import sys, threading

def run():
    dot = '.'
    sys.stdout.write(dot)
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write(dot)
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write(dot)
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write(dot)
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    thread = threading.Thread(target=run, args=())
    thread.start()
    word = ''
    while word != 'stop':
        word = input('banana\n')
        if word == 'exit':
            break

if __name__ == '__main__':
    main()
</code>
This one doesn't print . every second as it should. It stops threading.Thread and waits for the user to write. After that it prints . and then it
