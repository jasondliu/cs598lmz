import weakref
from typing import List, Tuple
from urllib.parse import urlparse, parse_qsl, urlencode
from urllib.request import urlopen

from .config import Config
from .lyricscache import Cache
from .lyricsgenius import Client, Lyrics
from .misc import notify
from .plugin import BaseLyricsProvider, SearchResult


class GeniusLyricsProvider(BaseLyricsProvider):
    __module__ = "lyricwikia"
    __version__ = "0.1.3"

    def __init__(self):
        super().__init__("genius", "Genius.com", "genius.png", "Search for lyrics on genius.com")
        self._config = Config("geniuslyrics")
        self._config.default("enable", False)
        self._config.default("key", "")
