import select
# Test select.select().

import select
import time

print 'When no input is ready, select blocks until input is ready'
print 'or the timeout occurs.  When input is ready, select does'
print 'not block.'

channel = select.kqueue()
channel.control([select.kevent(0,
                               select.KQ_FILTER_READ,
                               select.KQ_EV_ADD | select.KQ_EV_EOF)], 0)

print '[Blocking]'
start = time.time()
events = channel.control(None, 1, 1)
elapsed = time.time() - start
if events:
    print 'Elapsed:', elapsed, 'events:', events[0]
else:
    print 'Timeout'

channel.close()
