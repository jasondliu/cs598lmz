import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

if sys.version_info >= (3, 0):
    # Python 3
    def u(x):
        return x
else:
    # Python 2
    def u(x):
        return codecs.unicode_escape_decode(x)[0]

# Default is to not do any parsing
parse = None

# Do the parsing when the script is called as a main script
if __name__ == '__main__':
    import argparse
    import os
    import os.path
    import sys
    import time

    start_time = time.time()

    parser = argparse.ArgumentParser(
        description='Parse an XML document into a tree of Element objects',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--input', type=str,
        help='Input file (default: stdin)')
    parser.add_argument(
        '--output', type=str,
        help='Output file (default: std
