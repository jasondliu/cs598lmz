import codecs
codecs.register(Notification())


# Avoid spurious errors during `python setup.py test`, a la
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html:
try:
    __import__('multiprocessing')
except ImportError:
    pass


__author__ = 'Jared Kuolt'
__version__ = '0.1'


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


def make_env(file_name, *args):
    '''add version number and author name to setup.cfg file'''
    args += (
            ('version', __version__),
            ('author', __author__)
            )
    for k, v in args:
        file_name = file_name.replace('{{%s}}' % k, v)
    return file_name


def find_links():
    '''
