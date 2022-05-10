import select
import socket
import sys
import threading
import time

from gi.repository import GObject

from pychess.System import uistuff
from pychess.System.Log import log
from pychess.System.prefix import addDataPrefix
from pychess.Utils.const import (
    CHAT_ACTION,
    CHAT_TELL,
    CHAT_WHISPER,
    FICS_NONE,
    FICS_STANDARD,
    FICS_WILD,
    FICS_BLITZ,
    FICS_LIGHTNING,
    FICS_BUGHOUSE,
    FICS_CRAZYHOUSE,
    FICS_LOSERS,
    FICS_SUICIDE,
    FICS_ATOMIC,
    FICS_WILD8,
    FICS_WILD10,
    FICS_WILD12,
    FICS_WILD14,
    FICS_WILD16,
    FICS_WILD18,
    FICS_WILD20,
    FICS
