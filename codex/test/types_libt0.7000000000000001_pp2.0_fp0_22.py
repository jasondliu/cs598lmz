import types
types.ModuleType.__path__ = [path]

import subprocess
import os

if __name__ == '__main__':
    os.chdir(path)

    for d in filter(os.path.isdir, os.listdir(path)):
        if not d.startswith('.'):
            subprocess.call(['python', 'setup.py', 'install'], cwd=d)
