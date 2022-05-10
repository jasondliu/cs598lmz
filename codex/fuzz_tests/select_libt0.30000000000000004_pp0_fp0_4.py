import select
import sys

from . import __version__
from . import config
from . import log
from . import util
from . import xdg

logger = logging.getLogger(__name__)

_HELP = """\
Usage:
    {prog} [options] [<command> [<args>...]]
    {prog} --help

Options:
    -v, --version
    -h, --help
    -c, --config <file>
    -l, --log-level <level>
    -L, --log-file <file>
    -s, --socket <file>
    -p, --pid-file <file>
    -n, --no-daemon
    -d, --daemon
    -r, --reload
    -k, --kill
    -i, --interactive
    -e, --exec <command>
    -- <command> [<args>...]

Commands:
    help
    list
    start <name>
    stop <name>
    restart <name>
    reload
