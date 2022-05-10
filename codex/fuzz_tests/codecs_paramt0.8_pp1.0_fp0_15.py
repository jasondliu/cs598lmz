import codecs
codecs.register_error('truncated_utf_8', codecs.ignore_errors)

_PY3 = sys.version_info[0] == 3

if _PY3:
    def read_lines(file_handle, sizehint=None):
        fd = file_handle.fileno()
        if sizehint is None:
            sizehint = os.fstat(fd).st_size
        decoder = codecs.getincrementaldecoder('utf_8')('strict')

        offset = 0
        buffer = ''
        for b in iter(functools.partial(os.read, fd, sizehint - offset), ''):
            if offset + len(b) >= sizehint:
                buffer += decoder.decode(b, True)
                break

            buffer += decoder.decode(b)
            if decoder.needs_input:
                break

            offset += len(b)

        ret = buffer.splitlines(True)

        while True:
            buffer = decoder.decode(b'', True)
            if buffer
