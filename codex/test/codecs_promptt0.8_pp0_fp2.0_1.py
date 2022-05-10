import codecs
# Test codecs.register_error

def lookuperror(errorname, logname='<logfile>'):
    print(logname, errorname)
    return 'xxx', 0

codecs.register_error('test.lookuperror', lookuperror)

