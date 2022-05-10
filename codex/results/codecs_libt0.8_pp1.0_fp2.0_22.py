import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# ###


def get_attributes(meta_file):
    """Extracts the attributes of the given file.
    """
    attrib = {}
    if sys.version_info >= (3, 0):
        cmd = r'attrib "%s"' % meta_file
        result = subprocess.check_output(cmd, shell=True, universal_newlines=True).strip().split(' ')
        attrib = result[-1]

    return attrib


def set_attributes(meta_file):
    """Sets the attributes of the given file.
    """
    attrib = 'A'
    if sys.version_info >= (3, 0):
        cmd = r'attrib "%s" %s' % (meta_file, attrib)
        result = subprocess.check_output(cmd, shell=True, universal_newlines=True)

    return attrib


def make_sys_call(cmd, quiet=False):
