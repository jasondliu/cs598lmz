import codecs
# Test codecs.register_error for "surrogateescape" on all posix variants
# (Issue #3807)

try:
    codecs.register_error('surrogatestuff', codecs.surrogateescape_error)
    codecs.register_error('surrogatestuff2', codecs.surrogateescape_error)
except:
    # concurrent access to _codecs or name already used
    pass
else:
    def _check_register_error(encoding):
        with codecs.open(TESTFN, mode='w', encoding=encoding, errors='surrogateescape') as f:
            encoded = f.write('\udc80')
            f.close()
        with codecs.open(TESTFN, 'r', encoding=encoding, errors='surrogatestuff2') as f:
         
