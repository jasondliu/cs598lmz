import lzma
# Test LZMADecompressor
#
# This is a test script used for development purposes.

if __name__ == '__main__':
    import sys
    import os.path
    import argparse
    import time
    import zlib
    import lzma

    parser = argparse.ArgumentParser(description='Test LZMADecompressor')
    parser.add_argument('--chunksize', '-c', type=int, default=1024*1024,
                        help='Read data in chunks of this size')
    parser.add_argument('--compressed', '-z', action='store_true',
                        help='Test compressed data')
    parser.add_argument('--compress', '-Z', action='store_true',
                        help='Compress data')
    parser.add_argument('--decompress', '-D', action='store_true',
                        help='Decompress data')
    parser.add_argument('--filter', '-f', type=str, default='auto',
                        help='Filter to use')
