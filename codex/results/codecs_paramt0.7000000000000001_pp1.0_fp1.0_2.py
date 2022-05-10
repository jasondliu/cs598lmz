import codecs
codecs.register_error('strict', codecs.ignore_errors)


class CompileError(Exception):
    pass


def compile_file(filename, encoding=None):
    """
    Compile a Python source file and return the result.
    """
    if encoding is None:
        encoding = sys.getdefaultencoding()
    with open(filename, 'U') as f:
        return compile(f.read(), filename, 'exec', 0, True)


def compile_string(source, filename='<string>', mode='exec',
                   flags=0, dont_inherit=False):
    """
    Compile a Python source string and return the result.
    """
    return compile(source, filename, mode, flags, dont_inherit)


def compile_unicode(source, filename='<string>', mode='exec', flags=0,
                    dont_inherit=False, encoding='utf-8',
                    errors='strict'):
    """
    Compile a Python source string from Unicode and return the result.
    """
    return compile(source, filename, mode, flags
