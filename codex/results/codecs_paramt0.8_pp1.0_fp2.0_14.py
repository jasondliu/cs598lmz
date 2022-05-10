import codecs
codecs.register_error('replace_iso', codecs.lookup_error('replace'))

class AppArgumentParser(argparse.ArgumentParser):
    """
    A parser which converts from unicode to str type in argparse.
    This is useful for command line arguments in python scripts.
    """
    def convert_arg_line_to_args(self, arg_line):
        for arg in arg_line.split():
            try:
                yield arg.decode('utf-8')
            except UnicodeDecodeError as e:
                yield str(arg)


def to_unicode(string, encoding='utf-8'):
    if isinstance(string, unicode):
        return string
    else:
        return string.decode(encoding, 'replace_iso')


def to_utf8_str(string):
    """ Convert a unicode string into a utf-8 coded string. """
    if isinstance(string, unicode):
        return string.encode('utf-8', 'replace')
    else:
        return str(string)


def get_program_version
