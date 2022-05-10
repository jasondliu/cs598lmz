import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import __version__

from . import config
from . import util
from . import log
from . import cache
from . import db
from . import search
from . import web
from . import ui
from . import commands
from . import cmdparse
from . import player
from . import commands
from . import cmdline
from . import command
from . import completion
from . import help
from . import lyrics
from . import history
from . import playlist
from . import playlistcmd
from . import playlist_save
from . import playlist_load
from . import playlist_export
from . import playlist_import
from . import playlist_delete
from . import playlist_rename
from . import playlist_list
from . import playlist_info
from . import playlist_add
from . import playlist_remove
from . import playlist_move
from . import playlist_clear
from . import playlist_shuffle
from . import playlist_sort
from . import playlist_reverse
from . import playlist_copy
from . import playlist_diff
from . import playlist_intersect
from .
