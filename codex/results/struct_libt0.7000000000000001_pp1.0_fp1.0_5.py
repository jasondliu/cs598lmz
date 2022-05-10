import _struct

# Python 2/3 compatibility
try:
    range = xrange
except NameError:
    pass

# pylint: disable=too-many-locals,too-many-branches,too-many-statements
def run(filename, start_address, end_address, output=None, verbose=False):
    """
    Disassemble a binary file and generate an assembly output file.

    :param filename: the name of the binary file to disassemble
    :param start_address: the starting address of the disassembly (in hex)
    :param end_address: the ending address of the disassembly (in hex)
    :param output: the output file to write the assembly source to
    :param verbose: whether to print progress to stderr
    """
    # read the binary file into memory
    try:
        with open(filename, 'rb') as f:
            bytes_ = f.read()
    except IOError:
        sys.stderr.write('Error: unable to open {}\n'.format(filename))
        sys.exit(1)

