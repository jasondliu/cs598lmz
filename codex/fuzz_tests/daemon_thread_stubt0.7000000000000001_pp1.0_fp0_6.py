import sys, threading

def run():
    time.sleep(10)
    os.system('python '+sys.argv[1])

if __name__ == '__main__':
    r = threading.Thread(target=run)
    r.start()
    while True:
        time.sleep(1)
