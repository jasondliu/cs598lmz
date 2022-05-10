import codecs
# Test codecs.register_error and encodings.search_function for the
# name 'backslashreplace_error'
def backslashreplace_error(message):
    return (u'\\' * (len(message) + 4), len(message))
codecs.register_error('backslashreplace_error', backslashreplace_error)
import encodings

def test():
    print u'%s %s' % (1, 2)
    print u'%s %s' % (1, 2),

if __name__ == '__main__':
    import encodings
    encodings.search_function('ascii')
    test()
    #
    print
