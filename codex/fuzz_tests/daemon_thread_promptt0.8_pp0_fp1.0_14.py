import threading
# Test threading daemon mode to see if can kill it automatically after main thread exit
#
# Need to launch with `-u` to enforce unbuffered IO, otherwise the output
# won't be visible until after the program exits.

def foo():
    #while True:
    for i in range(5):
        print('foo')
        time.sleep(1)


def bar():
    for i in range(5):
        #while True:
        print('bar')
        time.sleep(1)

threads = [threading.Thread(target=foo), threading.Thread(target=bar)]

for t in threads:
    t.daemon = True
    t.start()

# If don't set
#   t.daemon = True
# the threads will keep running even main thread died
time.sleep(3)
print('main thread exit')
