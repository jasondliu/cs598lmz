fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = gi.__code__
fn.__code__.co_filename = "/tmp/test.py"
fn.__code__.co_name = "test"

for i in gi:
    pass
 
# This will throw an uncaught exception, which should be caught by the
# uncaught exception handler.

raise Exception("Test")
