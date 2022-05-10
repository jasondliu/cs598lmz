import gc, weakref

'''
#检测到内存泄漏时候的处理
@atexit.register
def goodbye():
    from pympler import tracker
    tr = tracker.SummaryTracker()
    tr.print_diff()
'''

def _received(data):   
    logger.debug("RECV:%d" % (len(data), ))
    return data

def _usend(date):
    logger.debug("SEND:%d" % (len(date), ))

def call_back(data, scoket):
    handle(data, scoket)
    gc.collect()
    
    
