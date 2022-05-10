import mmap
import os
import sys
import time
from collections import defaultdict
from datetime import datetime
from typing import List

from argparse import ArgumentParser
from pydoc import locate

from . import __version__
from . import config
from . import log
from . import utils
from . import version
from . import virtualenv
from . import wheel


def main(args=None):
    args = parse_args(args)
    config.initialize(args)

    if args.version:
        print("pip-compile version %s" % __version__)
        print("pip version %s" % version.get_pip_version())
        sys.exit(0)

    if args.generate_hashes:
        from .hashes import generate_hashes
        generate_hashes(args)
        sys.exit(0)

    if args.upgrade:
        from .upgrade import upgrade
        upgrade(args)
        sys.exit(0)

    if args.diff:
        from .diff import diff
        diff(args)
        sys
