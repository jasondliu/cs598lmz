import sys, threading

def run():
    for i in range(10):
        print(threading.current_thread().name, i)

def main():
    threading.Thread(target=run, name='thread1').start()
    threading.Thread(target=run, name='thread2').start()
    threading.Thread(target=run, name='thread3').start()
    threading.Thread(target=run, name='thread4').start()

if __name__ == '__main__':
    main()
