import threading
# Test threading daemon

def head(id, name):
    while True:
        print(id, name)
        if id > 0:
            time.sleep(1)

def tail():
    while True:
        stuff = input()
        if stuff == 'q':
            break
        print('You entered: {}'.format(stuff))

t0 = threading.Thread(target=head, args=(1, 'head0'))
t0_daemon = threading.Thread(target=head, args=(0, 'head1'))
t1 = threading.Thread(target=tail)

t1.start()
t0_daemon.start()
t0.start()

time.sleep(7)

print('Bye')

while True:
    time.sleep(1)
    print('...')
