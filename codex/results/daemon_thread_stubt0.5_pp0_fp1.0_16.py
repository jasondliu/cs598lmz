import sys, threading

def run():
    while True:
        try:
            print('hello')
        except:
            print('error')

if __name__ == '__main__':
    for i in range(4):
        t = threading.Thread(target=run)
        t.start()
