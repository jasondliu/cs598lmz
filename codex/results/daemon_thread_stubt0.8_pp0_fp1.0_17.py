import sys, threading

def run():
    global flag
    flag = True
    while flag:
        print(threading.active_count())
        print("Hello world")
        time.sleep(2)

if __name__ == '__main__':
    run()
