import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return id(a)

        def read(self):
            global a
            a = None
            raise ValueError()

    s = select.select([F()], [], [], 0)
    print("returned from select")

import codecs, encodings
import tokenize

FIXMES = True

class TestBadUnicode:
    # Check that str subclasses that screw up the unicode conversions
    # cause an error message.
    def setup_method(self, method):
        self.save_handlers = codecs.utf_8_encode, codecs.utf_8_decode
        self.save_bad_decode = encodings.utf_8.utf_8_decode
        encodings.utf_8.utf_8_decode = None
        self.save_bad_encode = encodings.utf_8.utf_8_encode
        encodings.utf_8.utf_8_encode = None
        codecs.utf_8_encode, codecs.utf_8_decode = None
