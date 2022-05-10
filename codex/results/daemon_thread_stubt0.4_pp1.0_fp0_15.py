import sys, threading

def run():
    while True:
        print(threading.current_thread().name)
        time.sleep(1)

def main():
    threading.Thread(target=run, name='Thread1').start()
    threading.Thread(target=run, name='Thread2').start()

if __name__ == '__main__':
    main()
