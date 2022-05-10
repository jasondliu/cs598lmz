import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a callback.

# Second collection should collect cyclic trash.

callback_called = False
def callback(x):
    global callback_called
    callback_called = True
mean_goodbye = '<arise Sir Knight, from thy long slumber>'

class Garbage:
    def __del__(self):
        pass
    def hello(self):
        global mean_goodbye
        print 'hello, good', mean_goodbye

def test_weakref():
    # setup circular garbage
    ob = Garbage()
    wr = weakref.ref(ob, callback)
    ob.hello()
    del ob
    gc.collect()
    assert callback_called

def callback_test(test, n):
    global callback_called
    callback_called = False
    test()
    assert callback_called

def no_callback_test(test, n):
    global callback_called
    callback_called = False
    test()
    assert not callback_called

def test_no_callback_callback_callback():
    for test, n in [(
