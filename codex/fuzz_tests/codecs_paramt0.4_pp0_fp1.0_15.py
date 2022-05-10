import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(path):
    """Reads a file and returns its contents."""
    f = codecs.open(path, encoding='utf-8', errors='strict')
    try:
        return f.read()
    finally:
        f.close()


def write_file(path, content):
    """Writes a file with the given content."""
    f = codecs.open(path, 'w', encoding='utf-8', errors='strict')
    try:
        f.write(content)
    finally:
        f.close()


def make_dir(path):
    """Creates a directory."""
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def remove_dir(path):
    """Removes a directory."""
    shutil.rmtree(path, ignore_errors=True)


def copy_dir(src_path, dst_path
