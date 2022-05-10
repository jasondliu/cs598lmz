import codecs
# Test codecs.register_error()
#
#      Written by Fredrik Lundh, January 1999
#
#      $Id: t_codecs_error.py,v 1.1 1999/01/28 15:24:45 fredrik Exp $

import codecs

def search(encoding):
    try:
        encoder = codecs.getencoder(encoding)
    except LookupError:
        encoder = None
    try:
        decoder = codecs.getdecoder(encoding)
    except LookupError:
        decoder = None
    print "%-10s encoder=%s decoder=%s" % (encoding, encoder, decoder)

def register_error(encoding, error):
    codecs.register_error(encoding, error)
    search(encoding)

search("ascii")
search("iso-8859-1")
register_error("iso-8859-1", "xmlcharrefreplace")
register_error("iso-8859-1", "ignore")
register_error("iso-8859-1", "
