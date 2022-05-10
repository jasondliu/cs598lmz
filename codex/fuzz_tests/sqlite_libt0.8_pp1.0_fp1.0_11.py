import ctypes
import ctypes.util
import threading
import sqlite3

from datetime import datetime
from subprocess import Popen
from subprocess import PIPE

from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.id3 import TRCK
from mutagen.id3 import TIT2
from mutagen.id3 import TALB
from mutagen.id3 import TPE1
from mutagen.id3 import TPE2
from mutagen.id3 import TCOM
from mutagen.id3 import TCON
from mutagen.id3 import TYER
from mutagen.id3 import COMM
from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC
from mutagen.id3 import error
from mutagen import File
from mutagen.mp4 import MP4
from mutagen.mp4 import MP4Cover
from mutagen.id3 import APIC
from mutagen.mp3 import EasyMP3 as MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen import File
from mutagen import Metadata
from mutagen.aac import AAC

