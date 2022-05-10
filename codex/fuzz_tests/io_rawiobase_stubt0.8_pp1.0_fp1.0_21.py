import io
class File(io.RawIOBase):
    '''A generic file interface to the TNG I/O API.  This is simply a
    wrapper around the C API call tng_util_fopen().

    See help(tng.tng.TNG) for usage examples.
    '''

    def __init__(self, file_name, mode=None, tng=None):
        '''
        Args:
            file_name: a string denoting the filename to read/write.
            mode: a string denoting whether to read or write the file. If a
                  write mode is given ('w', 'a', etc.) the TNG library will
                  attempt to create the file.
            tng: the TNG instance to use.  If None, then the default TNG
                 instance will be used.
        '''

        if tng is None:
            tng = get_default_tng()

        self._tng = tng
        self._file_name = file_name
        if mode is None:
            if file_name.endswith('.tng'):
                mode = 'r'

