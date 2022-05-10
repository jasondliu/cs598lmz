import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys, os
import urllib, urllib2
import json
import threading, time
import sqlite3

from PyQt4 import QtCore, QtGui

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_addaccount import Ui_AddAccountDialog
from ui.ui_addgroup import Ui_AddGroupDialog
from ui.ui_addpost import Ui_AddPostDialog
from ui.ui_addcomment import Ui_AddCommentDialog
from ui.ui_addlike import Ui_AddLikeDialog
from ui.ui_addfriend import Ui_AddFriendDialog
from ui.ui_addmessage import Ui_AddMessageDialog
from ui.ui_addphoto import Ui_AddPhotoDialog
from ui.ui_addvideo import Ui_AddVideoDialog
from ui.ui_addlink import Ui_AddLinkDialog
from ui.ui_addevent import Ui_AddEventDialog
