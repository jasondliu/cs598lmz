import weakref
import sys
import textwrap

from . import rpc
from . import rpc_pb2
from . import jwt
from . import mylogging
from . import memoize
from . import decorators
from . import pyjsonrpc

from apiclient.discovery import build
import httplib2
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

IMG_EXTS = ['.jpg', '.jpeg', '.png', '.gif', '.tiff']
AUDIO_EXTS = ['.m4a', '.mp3', '.wav']
VIDEO_EXTS = ['.m4v', '.wmv', '.mp4', '.avi', 'mpeg']
