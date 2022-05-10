fn = lambda: None
# Test fn.__code__.co_zombieframe
fn()

# Test with looping calls
def fn():
    return

l = task.LoopingCall(fn)
l.start(1)
l.stop()

# Test reference counting on some backends
# test_execnet

# Test defered's functions
d = defer.Deferred()
d.callback("test")
def _callback(res):
    pass
d.addCallback(_callback)

# Test task.deferLater
dl = task.deferLater(reactor, 0, _callback, "pong")
dl.addCallback(_callback)

# Test regex.compile
regx = regex.compile("^test$")

# Test Win32 API
#import win32api
#hResInfo = win32api.FindResource(None, test_dnd.REGISTER_DND_TYPES[0][-1], RT_TYPEDATA)
