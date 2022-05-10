import mmap
import os
import re
import sys
from subprocess import check_output

from . import __version__

from . import config
from . import errors
from . import utils


def main():
    """
    Main entry point for the application.
    """
    try:
        args = parse_args()
        if args.version:
            print(__version__)
            sys.exit(0)
        if args.debug:
            print(args)
        config.init(args)
        if args.debug:
            print(config.get())
        if args.command == "init":
            init(args)
        elif args.command == "add":
            add(args)
        elif args.command == "status":
            status(args)
        elif args.command == "diff":
            diff(args)
        elif args.command == "checkout":
            checkout(args)
        elif args.command == "commit":
            commit(args)
        elif args.command == "log":
            log(args)
        el
