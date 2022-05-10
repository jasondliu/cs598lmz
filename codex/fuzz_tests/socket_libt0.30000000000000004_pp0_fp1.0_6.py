import socket
import sys
import time
import threading
from threading import Thread
from threading import Lock
from threading import Condition

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

from ui_mainwindow import Ui_MainWindow
from ui_login import Ui_LoginDialog
from ui_register import Ui_RegisterDialog
from ui_chat import Ui_ChatDialog
from ui_chatroom import Ui_ChatroomDialog
from ui_addfriend import Ui_AddFriendDialog
from ui_addgroup import Ui_AddGroupDialog
from ui_addgroupmember import Ui_AddGroupMemberDialog
from ui_groupchat import Ui_GroupChatDialog

from user import User
from chatroom import Chatroom
from group import Group
from message import Message
from message import MessageType
from message import MessageStatus
from message import MessageContent
from message import MessageContentType
from message import MessageContent
