import sys, threading

def run():
    p = multiprocessing.Process(target=test_BaseManager.use_BaseManager, args=(test_BaseManager.token, queue))
    p.start()
    p.join()
    assert queue.get() == test_BaseManager.token

#
# Test that BaseManager.Queue works
#

queue = multiprocessing.managers.BaseManager().Queue()
run()

#
# Test that BaseManager.Queue works with a proxy
#

mgr = multiprocessing.managers.BaseManager()
p = multiprocessing.Process(target=test_BaseManager.use_BaseManager, args=(mgr, test_BaseManager.token, queue))
p.start()
p.join()
assert queue.get() == test_BaseManager.token

print 'done'
