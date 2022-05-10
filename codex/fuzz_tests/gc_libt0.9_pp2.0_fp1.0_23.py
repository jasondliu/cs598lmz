import gc, weakref
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader, Sound

from kivy.properties import AliasProperty, ListProperty

from loader import load_widget
load_widget("playlist.kv")
load_widget("player.kv")
load_widget("songinfo.kv")
load_widget("notibox.kv")

import xUtils


def _get_free_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port


class SongInfo(BoxLayout):
    def __init__(self, song, **kwargs):
        self.isExpanded = False
        super(SongInfo, self).__init__(**kwargs)

    def expand(self):
        if self.isExpanded:
            return
        self.isExpanded = True
