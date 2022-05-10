import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import utils
from . import settings
from . import __version__

from .logger import Logger
from .config import Config
from . import config
from . import plugin
from . import commands
from . import commands_help
from . import commands_history
from . import commands_tab_completion
from . import commands_config
from . import commands_plugin
from . import commands_misc
from . import commands_alias
from . import commands_search
from . import commands_file
from . import commands_download
from . import commands_playlist
from . import commands_stream
from . import commands_resume
from . import commands_command
from . import commands_process
from . import commands_clear
from . import commands_remote
from . import commands_server
from . import commands_list
from . import commands_lyrics
from . import commands_lyrics_search
from . import commands_lyrics_download
from . import commands_lyrics_show
from . import commands_lyrics_edit
from . import commands_lyrics_save
