import sys, threading

def run():
    for i in range(1,4):
        time.sleep(1)
        msg = 'T' + str(i)
        print(msg, end=' ')
        sys.stdout.flush()
    print('\n')

def run2():
    for i in range(1,4):
        time.sleep(1)
        msg = 'T' + str(i)
        print(msg, end=' ')
        sys.stdout.flush()
    print('\n')

print('\nStart')

t = threading.Thread(target=run)
t.start()

t2 = threading.Thread(target=run2)
t2.start()

print('\nEnd')
