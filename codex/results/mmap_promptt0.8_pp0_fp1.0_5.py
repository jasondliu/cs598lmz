import mmap
# Test mmap.mmap support
try:
    test_mmap_file = open(tempfile.mkstemp()[1], 'w+b')
    test_mmap = mmap.mmap(test_mmap_file.fileno(), 8)
    MMAP_SUPPORTED = True
except:
    MMAP_SUPPORTED = False
finally:
    test_mmap.close()
    test_mmap_file.close()

def get_random_bytes(length):
    """
    Generate a random string of bytes of a certain length.
    :param length: The length of bytes to generate.
    :return: A string of random bytes.
    """
    random_bytes = []
    for _ in xrange(length):
        random_bytes.append(chr(random.randint(0, 255)))
    return ''.join(random_bytes)

def get_random_string(length, alphabet=None):
    """
    Generate a random string of length N using the given alphabet.
    :param length: The length of the string to generate.
    :
