import codecs
# Test codecs.register_error
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
# *** Checked by test_codecs.py ***

import codecs,sys

def test(name,errors='strict'):
    print '-'*30+'\n%s' % name
    e = codecs.lookup(name).encode('abc',errors)[0]
    print 'encoded:',`e`
    print 'decoded:',e.decode(name,errors)

print
print 'Test codecs.register_error...'
print

# Register an error handler that just works on the exceptions:

def ignore_errors(e):
    if isinstance(e, UnicodeEncodeError):
        return (u'',e.end)
    elif isinstance(e, UnicodeDecodeError):
        return (u'',e.end)
    elif isinstance(e, UnicodeTranslateError):
        return (u'',e.end)

