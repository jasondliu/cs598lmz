import weakref
import os
import geodat
import icons
import logger
import utils
import netutils

from pyspatialite import dbapi2 as sqlite3
from qgis.core import *
from qgis.utils import iface
from qgis.gui import QgsMessageBar
from geogigTransaction import GeogigTransaction
from geogigexception import GeoGigException
from geogiglog import GeogigLog
from dialog import CommitDialog, PushDialog, PullDialog, FetchDialog
from dialog import MergeDialog, ConflictDialog, CloneDialog
from geogigutilstest import GeogigUtilsTest

class ProjectInfo():
    def __init__(self, repo="", projName="", projPath="", mode="", hash="", currentUser="", srid="", authid="", options=None):
        self.repo = repo
        self.version = ""
        self.projName = projName
        self.projPath = projPath
        self.mode = mode
        self.hash = hash
        self.currentUser = current
