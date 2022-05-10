import codecs
codecs.register_error('strict', codecs.ignore_errors)


def read_file(filename):
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        return f.read()


def write_file(filename, contents):
    with codecs.open(filename, 'w', encoding='utf-8') as f:
        f.write(contents)


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = read_file(os.path.join(package, '__init__.py'))
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
   
