import codecs
# Test codecs.register_error()

import sys
if sys.platform == 'darwin':
    # The Mac OS X 10.3.9 codecs.register_error() implementation
    # doesn't support 'replace' and 'ignore' error handlers.
    #
    # This is fixed in Mac OS X 10.4, so this test is skipped
    # when running on Mac OS X 10.4 or later:
    import platform
    darwin = platform.mac_ver()
    if darwin[0] >= '10.4':
        raise TestSkipped("codecs.register_error() broken on Mac OS X 10.3.9")

def test(encoding):
    errors = [
        ('strict', None),
        ('ignore', None),
        ('replace', None),
        ('xmlcharrefreplace', None),
        ('backslashreplace', None),
        ('namereplace', None),
        ('testdecodeerrorhandler', ''),
        ('testencodeerrorhandler', ''),
        ('testdecodeerrorhandler', 'replace'),
        ('testencodeerrorhandler', 'replace'),

