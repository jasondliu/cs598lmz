import sys, threading

def run():
    os.system('python3 server.py')

def main():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    time.sleep(2)
    os.system('python3 client.py')

if __name__ == '__main__':
    main()
