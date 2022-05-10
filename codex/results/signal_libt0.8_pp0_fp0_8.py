import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import json
import argparse
import datetime
from typing import List

from colorama import init

from jornal.article import Article
from jornal.conf import JornalConfig
from jornal.entry import Entry
from jornal.exceptions import JornalException
from jornal.entry_manager import EntryManager
from jornal.entry_renderer import EntryRenderer
from jornal.journal import Journal


class Cli:
    """
    The main CLI class that is the entry point for the command line interface.
    """

    def __init__(self, arguments: List[str] = None):
        """
        Initialize the CLI and parse the arguments provided.
        :param arguments: The arguments passed on to the CLI.
        """
        init()
        self.arguments = arguments if arguments is not None else sys.argv[1:]
        self.parser = self.create_parser()
        self.args = self.parser.parse_args(self.arg
