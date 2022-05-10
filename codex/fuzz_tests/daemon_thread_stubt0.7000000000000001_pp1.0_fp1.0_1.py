import sys, threading

def run():
    while True:
        i = 0
        while i < 100:
            print('\r{:^5.2f}%'.format(i))
            time.sleep(0.1)
            i += random.uniform(0, 0.5)
        print('\rDone!')
        time.sleep(1)

def main():
    if len(sys.argv) < 2:
        print('Please enter a command.')
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == 'run':
        t = threading.Thread(target=run)
        t.start()

if __name__ == '__main__':
    main()
