import sys, threading

def run():
    for i in range(10, 0, -1):
        print(i)
        sys.stdout.flush()
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()

    input('Press enter to quit')
