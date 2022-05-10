import lzma
# Test LZMADecompressor class.

class LZMADecompressorTester(object):
    """Test LZMADecompressor class"""

    # no args -> get file name from stdin
    # one arg -> get file name from arg
    def get_filename(self, argv):
        """Get file name from args"""
        if len(argv) == 1:
            return sys.stdin.name
        elif len(argv) == 2:
            return argv[1]
        else:
            raise ValueError('Usage: lzmald.py [file.lzma]')

    def main(self, argv=None):
        """main function"""

        if argv is None:
            argv = sys.argv
        filename = self.get_filename(argv)
        with open(filename, 'rb') as input_file:
            decompressor = lzma.LZMADecompressor()
            #compress_size = 0
            #output_size = 0
