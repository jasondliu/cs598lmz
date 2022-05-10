import socket
import sys
import datetime
import time
import threading
import json
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from client.ui.mainwindow import Ui_MainWindow
from client.ui.login import Ui_LoginForm
from client.ui.register import Ui_RegisterForm
from client.ui.userinfo import Ui_UserInfoForm
from client.ui.friendinfo import Ui_FriendInfoForm
from client.ui.addfriend import Ui_AddFriendForm
from client.ui.chatwindow import Ui_ChatWindow
from client.ui.chatroomwindow import Ui_ChatRoomWindow
from client.ui.chatroom import Ui_ChatRoomForm
from client.ui.createchatroom import Ui_CreateChatRoomForm
from client.ui.userlist import Ui_UserListForm
