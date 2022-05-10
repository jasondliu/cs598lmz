import codecs
# Test codecs.register_error

def my_replace(exc):
    s = [u'\ufffd'] * (exc.end - exc.start)
    if exc.object[exc.start] == '\xa0':
        s[0] = u' '
    return (u''.join(s), exc.end)

def my_ignore(exc):
    pass

def my_xmlcharrefreplace(exc):
    return ('&#%d;' % ord(exc.object[exc.start]), exc.end)

def my_namereplace(exc):
    if exc.end - exc.start == 1:
        return ('name', exc.end)
    else:
        return ('name' * (exc.end - exc.start), exc.end)

def my_backslashreplace(exc):
    return ('\\' * (exc.end - exc.start), exc.end)

def my_raise(exc):
    if isinstance(exc, UnicodeError):
        raise TypeError
    else:
        raise exc

