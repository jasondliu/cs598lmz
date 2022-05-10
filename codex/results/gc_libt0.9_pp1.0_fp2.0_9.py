import gc, weakref, logging

from .boot import (boot_root_mount, build_boot_info, final_deferred,
                   include_boot_parser)

from . import cache
from . import cleanup
from . import sources


class ImageDestination:
    '''Context manager that creates an image to be mounted locally.'''

    _LOG_NAME = 'ignition'
    _DEST = 'dest'

    CACHE_SIZE = 60

    VARIANTS_HELP = dedent("""\
        Each of the following variants control a different feature of the resulting
        initramfs:

          initrd           Include the minimal set of tools required for an initramfs
          network          Include network tools (ifupdown, resolvconf)
          fs               Include fs tools (e2fsprogs, jfs, xfs, btrfs)
          debug            Include debug tools (strace, lsof)
          cloud-init       Inlucde cloud-init

        You can set variants by simply specifying them as a space-separated list,
        e.g., "initrd network" or "
