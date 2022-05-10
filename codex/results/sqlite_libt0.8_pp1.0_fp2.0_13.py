import ctypes
import ctypes.util
import threading
import sqlite3
import time
from pathlib import Path
from datetime import datetime
from pprint import pprint as pp

from pw.common.utils import log

from pw.models.profile import Profile
from pw.models.site import Site
from pw.models.entry import Entry
from pw.models.attachment import Attachment
from pw.models.attachment_entry import AttachmentEntry

from pw.lib.time import Time
from pw.lib.password import Password
from pw.lib.entry import Entry as EntryLib
from pw.lib.site import Site as SiteLib
from pw.lib.profile import Profile as ProfileLib
from pw.lib.exceptions import EntryNotFound, ProfileNotFound
from pw.lib.attachment import Attachment as AttachmentLib

from pw.ui.utils.widgets import WidgetUtils

logger = log.create_logger(__name__)

class CoreThread(threading.Thread):
    def __init__(self, core):
        self.app = core.app
        self.
