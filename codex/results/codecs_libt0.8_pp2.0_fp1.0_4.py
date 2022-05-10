import codecs
codecs.register_error('cosine', CosineSimilarity)


class CosineSimilarity(Exception):
    def __init__(self):
        pass

    def encode(self, input):
        if not isinstance(input, str):
            raise TypeError
        return input.encode('utf-8', 'strict')

    def decode(self, input):
        if not isinstance(input, bytes):
            raise TypeError
        return input.decode('utf-8', 'cosine')


print(codecs.escape_encode(b'\xfe\xff\x00\x41'))
print(codecs.escape_decode(b'\xFE\xFF\x00\x41'))
# (b'\\xfe\\xff\\x00A', 4)
# (b'\xff\xfe\x00\x41', 4)


def search(pattern, text):
    '''
    non-overlapping search
    '''
    if len(pattern) > len(text):
        return -1
    for i
