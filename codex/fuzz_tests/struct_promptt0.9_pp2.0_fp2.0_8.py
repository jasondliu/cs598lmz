import _struct
# Test _struct.Struct.format_size
# See [14148]
class C(object):
    def __init__(self, code):
        self.code = code
        self.fmt = _struct.Struct(code)
        # The size of the structure cannot be known when an opaque data type is
        # specified
        if (('c' in code) or ('s' in code) or ('p' in code)):
            self.size = None
        else:
            self.size = self.fmt.size
    def __str__(self):
        return '_struct.Struct(%r)' % self.code

tests = [
    C('x'),
    C('c'),
    C('b'),
    C('B'),
    C('h'),
    C('H'),
    C('i'),
    C('I'),
    C('l'),
    C('L'),
    C('f'),
    C('d'),
    C('s'),
    C('p'),
    C('cc'),
    C('hh'),
    C('iii'),
    C('lll
