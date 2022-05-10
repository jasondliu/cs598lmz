import codecs
# Test codecs.register_error(name,handler)

def encode(input,errors='strict'):
    return (input.encode('ascii','xmlcharrefreplace'), len(input))

def decode(input,errors='strict'):
    return (input.decode('ascii','replace'), len(input))

codecs.register_error('test', codecs.lookup_error('strict'))
codecs.register_error('xmlcharrefreplace', codecs.lookup_error('xmlcharrefreplace'))

