import io
# Test io.RawIOBase support
import io
# Test io.FileIO support
import io
import array
# Test bytearray support

# cStringIO.StringIO should work out of the box
import cStringIO

# read to a buffer
import urllib2

# Requests
import requests
# Requests (urllib3)
import requests.packages.urllib3

# Requests dependency
import requests.sessions
# pyOpenSSL dependency
import OpenSSL


# Restricted test
def test_restricted():
    from RestrictedPython import compile_restricted
    from RestrictedPython import safe_builtins
    from RestrictedPython import utility_builtins
    from RestrictedPython import restrictions

    @restrictions.Restrictions()
    def test(code):
        co = compile_restricted(
            '"%s"\n' % code,
            'test', 'single'
        )
        print('RestrictedPython version: %s' % restrictions.VERSION)
        co_ns = safe_builtins.copy()
        co_ns.update(utility_builtins)
