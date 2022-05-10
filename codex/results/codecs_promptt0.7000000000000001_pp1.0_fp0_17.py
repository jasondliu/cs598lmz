import codecs
# Test codecs.register_error() in a different module, issue #6769
globals()['register_error'] = codecs.register_error
globals()['lookup_error'] = codecs.lookup_error

# Test for issue #6865
# A codec search function for the base64 module.
from codecs import lookup
globals()['base64_lookup'] = lookup

# Test for issue #6886
# Test for the 'translate' argument to the IncrementalEncoder.
from codecs import IncrementalEncoder
globals()['IncrementalEncoder'] = IncrementalEncoder

from codecs import EncodedFile
globals()['EncodedFile'] = EncodedFile

# Test for issue #1512
import locale, codecs
encoding = locale.getpreferredencoding()
globals()['test_1512_encode'] = codecs.getencoder(encoding)
globals()['test_1512_decode'] = codecs.getdecoder(encoding)

# Test for issue #1300
import codecs
def test_
