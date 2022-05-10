import select
import logging
import re

from . import config
from . import error
from . import util
from . import zfs
from .ssh import Ssh
from .zfs import snapshot_name_parse
from .zfs import clone_name_parse
from .zfs import filesystem_name_parse
from .zfs import snapshot_name
from .zfs import filesystem_name
from .zfs import filesystem_get_snapshots

log = logging.getLogger(__name__)
config.declare_config_parameter(
	"post_snapshot_command",
	"Command executed after a snapshot.",
	None);

def flush_stdin():
	while select.select([sys.stdin.fileno()], [], [], 0)[0]:
		sys.stdin.read(1)

