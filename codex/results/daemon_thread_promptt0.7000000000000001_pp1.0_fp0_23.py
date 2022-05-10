import threading
# Test threading daemon
def test(n):
    while True:
        print('Thread %d' % n)
        time.sleep(1)

for i in range(5):
    t = threading.Thread(target=test, args=(i,))
    t.setDaemon(True)
    t.start()

# Test threading event
def wait_for_event(e):
    '''Wait for the event to be set before doing anything'''
    print('wait_for_event starting')
    event_is_set = e.wait()
    print('event set: %s' % event_is_set)

def wait_for_event_timeout(e, t):
    '''Wait t seconds and then timeout'''
    while not e.isSet():
        print('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        print('event set: %s' % event_is_set)
        if event_is_set:
            print('processing event')
        else:
            print('doing other things')


