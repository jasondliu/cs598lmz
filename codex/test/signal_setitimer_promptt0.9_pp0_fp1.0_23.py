import signal
# Test signal.setitimer to generate sigalarm interruptions
# As we don't want these to cause an exception, we want to determine if we
# are in a signal handler and in that case, just continue
#############################
import StringIO

_threads = threading.local()

def currentThread():
    threadId = get_ident()
    try:
        return _threads.value[threadId]
    except KeyError:
        #print "Exception in currentThread ", sys.exc_info()
        return None

def getOrCreateThreadObject(threadId):
    #print "Creating thread object for %x" % threadId
    _threads.value[threadId] = threadObject_t(threadId)
    return _threads.value[threadId]

_threadObjectPool = []
def _releaseThreadObject(th):
    _threadObjectPool.append(th)

# This class is used by threads created by the threading module
class threadObject_t(object):
    def __init__(self, id):
        self.id = id
