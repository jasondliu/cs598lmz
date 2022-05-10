import lzma
lzma_mode = lzma.FORMAT_XZ

# test
from pathlib import Path
home_dir: Path = Path('/Users/catx0rr/workspace')
from diva.layout import injector
from diva.config import conf
from diva import config
from diva.layout import layouts
from diva.media import media_types
from diva.grabber import Grabber
from diva.db import sql
import logging
from diva.grabber.plugins import youtube
from diva.grabber.plugins import myvideo
from diva.grabber.plugins import shuu
from diva.grabber.plugins import sic
from diva.grabber.plugins import pro7
from diva.grabber.plugins import javlib

# let's go
logging.basicConfig(level=logging.DEBUG)
conf.init(home_dir)
layouts.create_layout()
config.init('core')

# sql
sql.init(conf.database_path, [])
sql.get_conn().execute('''
INSERT INTO media (
