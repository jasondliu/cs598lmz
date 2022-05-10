import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_file_size(fname):
    """Return file size in bytes."""
    fsize = 0
    with codecs.open(fname, 'rb', 'utf-8', 'strict') as fin:
        fin.seek(0, os.SEEK_END)
        fsize = fin.tell()
    return fsize

def _read_file(fname):
    """Read file and return its contents."""
    content = ''
    with codecs.open(fname, 'rb', 'utf-8', 'strict') as fin:
        content = fin.read()
    return content

def _write_file(fname, content):
    """Write content to file."""
    with codecs.open(fname, 'wb', 'utf-8', 'strict') as fout:
        fout.write(content)

def _get_file_list(root_dir):
    """Return list of file names in root_dir."""
    file_list = []
    for
