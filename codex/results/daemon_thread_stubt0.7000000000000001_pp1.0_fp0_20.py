import sys, threading

def run():
    print('running')

threading.Thread(target=run).start()

if __name__ == "__main__":
    print('__main__')
