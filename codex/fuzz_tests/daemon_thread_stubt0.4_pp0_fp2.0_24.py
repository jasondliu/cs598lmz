import sys, threading

def run():
    while True:
        try:
            print(threading.current_thread())
            a = input()
            print(a)
        except:
            print('exception')
            break

def main():
    t = threading.Thread(target=run)
    t.start()
    t.join()

if __name__ == '__main__':
    main()
