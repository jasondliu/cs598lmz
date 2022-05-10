import sys, threading

def run():
    for i in range(10):
        print('{}'.format(i))
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
