import io
class File(io.RawIOBase):
    # Code for _fileio object is taken from posixmodule.c


    def _set_mode(self, mode):
        # Internal helper for constructor.  Returns the file descriptor
        # for the new file.

        if not isinstance(mode, basestring):
            raise TypeError('invalid mode: %r' % mode)

        file_flags = _os.O_RDONLY

        # Parse the mode string.
        # Note that we don't handle 'U', 'rU' and 'Uu' right now.
        flag_modes = (
            # (universal_newlines, binary)
            ('t', False),
            ('b', True),
        )

        flag_modes_default = flag_modes[0]

        # handle the first character
        ch = mode[0:1]
        if ch == 'r':
            pass
        elif ch == 'w':
            file_flags = _os.O_WRONLY | _os.O_CREAT | _os.O_TRUNC
            flag_modes_default =
