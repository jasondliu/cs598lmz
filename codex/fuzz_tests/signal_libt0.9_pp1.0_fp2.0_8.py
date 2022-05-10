import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Trying to deal with type hinting on Travis by uninstalling `typing`.
# Anaconda3 has a different version of type hinting
# Raises an error in anaconda version 3.5
try:
    import typing
    import sys

    # This module will throw error if it is not uninstalled.
    # See http://docs.python.org/3/library/typing.html
    sys.modules.pop('typing')
except:
    pass

try:
    import aiida

    # This will print the first and last commit messages from the AiiDA
    # installation that is loaded.
    import os
    import subprocess
    from aiida.backends.utils import get_backend_from_manager
    import os.path

    repo_dir = os.path.dirname(os.path.dirname(aiida.__path__[0]))

    def get_commits_hash(repo_dir):
        '''Return a list with the first
