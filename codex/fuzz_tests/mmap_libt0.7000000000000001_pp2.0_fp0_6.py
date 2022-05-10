import mmap
import os
import subprocess
import tempfile
import time

from . import config
from . import util

# The number of seconds to wait for the watcher to die after a SIGTERM.
TERMINATION_TIMEOUT = 5


def _get_watcher_script(args):
    """Returns the contents of the watcher script.

    Args:
        args: Command-line arguments.

    Returns:
        The watcher script.
    """
    # The script uses a shebang with bash, but it uses some bash-isms that
    # aren't present in macOS's default shell, so we explicitly use bash.
    #
    # The script needs to detect when no more files are being watched. It's
    # important that it detect this even if the watcher dies, since we need to
    # kill the watcher and start a new one. We can't use the "inotifywait"
    # option "-e delete_self" to detect when the inotify file descriptor is
    # closed, because it doesn't work on pipes.
    #
    # The script uses the "in
