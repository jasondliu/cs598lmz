import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time
import sys

from lib.main import _
from lib.utils import frange, remove_accents, nonl, get_max_id
from lib.gif import GIF
from lib.functions import clear_caption
from lib.xml_sax_parser import XML_sax_parser
from lib.parsed_caption_item_info import Parsed_caption_item_info
from lib.caption_item import Caption_item
from lib.caption_info import Caption_info
from lib.clip_info import Clip_info
from lib.project_file import Project_file
from lib.codecs import Codecs
from lib.project_data import Project_data
from lib.global_vars import app_config
from lib.constants import CAPTION_ITEM_CLASS_DICT
from lib.auto_updater import Auto_updater


log = logging.getLogger("CaptionMaker")


class CaptionMaker:
    """
    Main CaptionMaker class.
    """

