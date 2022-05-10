import types
types.ModuleType.__new__ = lambda cls, name, bases, namespace: cls(name, bases, namespace)
del types

# setup the root logger
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.info("%s started" % __name__)


def get_file_contents(path):
    with open(path, 'r') as f:
        return f.read()

def get_file_attributes(path):
    attributes = {}
    for name in 'st_mode st_ino st_dev st_nlink st_uid st_gid st_size st_atime st_mtime st_ctime'.split():
        attributes[name] = getattr(os.stat(path), name)
    return attributes

def get_file_type(path):
    return os.stat(path).st_mode

