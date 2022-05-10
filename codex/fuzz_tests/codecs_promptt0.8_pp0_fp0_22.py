import codecs
# Test codecs.register_error
import test.test_support
test.test_support.verbose = 0

def f_strict(message): raise UnicodeError(message)
def f_ignore(message): return (u'z', message.start + 1)
def f_replace(message): return (u'\ufffd', message.start + 1)

def test(name, input, errors, output):
    print "Trying encoder", name
    encoder = codecs.getencoder(name)
    codecs.register_error(name, f_strict)
    try:
        x = encoder(input, errors)
        raise Exception, "encoding did not fail with 'strict'"
    except UnicodeError:
        pass
    codecs.register_error(name, f_ignore)
    x = encoder(input, errors)
    if x != output:
        raise Exception, "encoding with 'ignore' gave %r, expected %r" % (x, output)
    codecs.register_error(name, f_replace)
    x = encoder(input, errors)

