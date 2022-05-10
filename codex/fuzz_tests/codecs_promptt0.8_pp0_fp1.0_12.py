import codecs
# Test codecs.register_error
import doctest

# Test the doctest for the current module
def test():
    doctest.testmod()
    return None

if __name__ == '__main__':
    test()
