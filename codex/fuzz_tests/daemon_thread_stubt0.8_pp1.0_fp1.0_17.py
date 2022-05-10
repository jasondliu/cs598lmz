import sys, threading

def run():
    run = os.system('sqlmap -r '+var)

if __name__ == '__main__':
    var = input('Enter Request File: ')
    run()

if __name__ == '__main__':
    var = input('Enter Request File: ')
    for i in range(100):
        p = threading.Thread(target=run, args=())
        p.start()
