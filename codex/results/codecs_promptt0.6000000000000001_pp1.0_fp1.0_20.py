import codecs
# Test codecs.register_error('myerror', myerrorhandler)

def myerrorhandler(exception):
    print("myerror: %r" % exception)
    return (b'', exception.start + 1)

codecs.register_error('myerror', myerrorhandler)

print("'foobar' with myerror: %a" % 'foobar'.encode('ascii', 'myerror'))

# Test codecs.register_error('myerror2', myerrorhandler2)

def myerrorhandler2(exception):
    print("myerror2: %r" % exception)
    return (b'!', exception.end)

codecs.register_error('myerror2', myerrorhandler2)

print("'foobar' with myerror2: %a" % 'foobar'.encode('ascii', 'myerror2'))

# Test codecs.register_error('myerror3', myerrorhandler3)

def myerrorhandler3(exception):
    print("myerror3: %r" % exception)
    return (b'!
