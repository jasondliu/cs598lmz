import io
# Test io.RawIOBase implementations.
# For now, we mostly test SFIO (FastCGI), *not* io.FileIO().
# IO behaviors are described in https://www.python.org/dev/peps/pep-0471/

# TODO: Eventually, it would be good to do testing with multiple processes
# (to make sure the file handles don't "see" each other!  This might require
# us to make our own FastCGI implementation in Python, instead of testing
# with a pre-built binary like apache + mod_fcgid).  The python standard
# library has a multiprocessing module, but I don't know how to test it
# without first implementing an iterator in Python for a server.
# see: https://docs.python.org/3/library/multiprocessing.html
#      https://pymotw.com/3/multiprocessing/basics.html

def run_io_tests(io_inst):
    """ Test RawIOBase implementations! """
    print("==================================")
    print(io_inst.__class__)
    io_
