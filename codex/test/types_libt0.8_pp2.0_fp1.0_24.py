import types
types.SimpleNamespace

from pathlib import Path
import fnmatch


def hello():
    """
    Hello.
    """
    print('world')


def find_files(path, pattern):
    """ Find files

    This function finds files in path (recursively) that matches
    a given pattern.
    """
    path = Path(path).expanduser()
    for filename in path.glob('**/*'):
        if fnmatch.fnmatch(filename, pattern):
            yield filename
