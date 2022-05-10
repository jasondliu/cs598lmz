import sys, threading

def run():
    while True:
        input()
        print('[*] Done')
        sys.exit()

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()

    while True:
        time.sleep(1)
        print('[*] Working...')
