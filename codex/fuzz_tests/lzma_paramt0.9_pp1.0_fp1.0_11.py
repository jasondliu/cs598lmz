from lzma import LZMADecompressor
LZMADecompressor._decompress = nop_patcher(LZMADecompressor._decompress)

from pyvmf import map_parse

import bs4
import requests
from engine import Engine as Engine
from urllib.request import urlopen


class Workshop_Downloader(Command):
    def __init__(self):
        super().__init__()
        self.name = 'workshop'
        self.help = 'Downloads a specific map from the workshop.'
        self.syntax = 'workshop [id] <direct>'
        self.flag = 0

    @asyncio.coroutine
    def execute(self, player, arguments):
        if len(arguments) == 0:
            player.tell("Syntax: workshop [id] <direct>")
            return

        id = arguments[0]
        direct = False

        if len(arguments) > 1:
            direct = True

        if len(arguments) == 2 and arguments[1].lower() != 'direct':
            player.tell("Syntax: workshop [id] <direct>
