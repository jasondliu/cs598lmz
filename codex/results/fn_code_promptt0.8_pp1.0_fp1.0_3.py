fn = lambda: None
# Test fn.__code__, fn.__closure__, fn.__dict__ and fn.__globals__
fn.__code__
fn.__closure__
fn.__dict__
fn.__globals__

db = {}
def new_printer(name):
    def printer():
        print "Hi, I'm %s" % name
    db[name] = printer
    return printer

fred = new_printer('Fred')
fred()
db['Fred']()
