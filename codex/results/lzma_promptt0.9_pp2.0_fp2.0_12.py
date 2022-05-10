import lzma
# Test LZMADecompressor - decompress(). Here we decompress the file created in
# test_compress_onefile.

LOG_DIRECTORY = "log_test_compress_onefile/"

try:
    os.mkdir(LOG_DIRECTORY)
except OSError:
    pass

class Log(object):
    """File like for writing to a thread specific log.

    Output looks like:
    >>> $ cat log_test_compress_onefile/0.log
    >>> Thread-0
    >>> Thread-0
    >>> ^D
    >>> $ cat log_test_compress_onefile/1.log
    >>> Thread-1
    >>> Thread-1
    >>> ^D

    Some resolution of issue 5220 could help with cleanup here.
    """

    def __init__(self):
        self.logfile = open(os.path.join(LOG_DIRECTORY, "%d.log" %
                                        (thread.get_ident(),)), "w")

    def __del__(self):
        self.logfile.close()

    def write(self,
