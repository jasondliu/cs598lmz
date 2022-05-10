import gc, weakref
from contextlib import contextmanager

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build, Resource
from googleapiclient.http import MediaFileUpload
from apiclient import errors
from boxsdk import OAuth2, Client, JWTAuth
from boxsdk.object.collaboration import CollaborationRole


from filebrowser.drive import Drive
from filebrowser.box import Box


class Manager(QtCore.QObject):
    started = QtCore.Signal()
    stopped = QtCore.Signal()
    loggedIn = QtCore.Signal(str)
    loggedOut = QtCore.Signal(str)
    ready = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self._running = False
        self._settings = QtCore.QSettings("AzureFlight", "FileBrowser")
        self._box_apps = self.LoadBoxApps()
        self._users = dict()

