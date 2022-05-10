import sys, threading

def run():
    print('run')
    time.sleep(60)
    print('complete')

def main():

    working_thread = threading.Thread(target=run)
    working_thread.daemon = True
    working_thread.start()
    print(working_thread.getName())
    while True:
        time.sleep(0.1)

if __name__ == '__main__':
    main()
