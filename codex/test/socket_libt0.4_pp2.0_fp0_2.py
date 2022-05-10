import socket
import sys
import time
import threading
import os
import shutil
import struct
import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_mainwindow import Ui_MainWindow
from ui_login import Ui_Login
from ui_register import Ui_Register
from ui_chat import Ui_Chat
from ui_chatroom import Ui_ChatRoom
from ui_chatroom_add import Ui_ChatRoom_Add
from ui_chatroom_add_member import Ui_ChatRoom_Add_Member
from ui_chatroom_chat import Ui_ChatRoom_Chat
from ui_chatroom_chat_file import Ui_ChatRoom_Chat_File
from ui_chatroom_chat_image import Ui_ChatRoom_Chat_Image
from ui_chatroom_chat_video import Ui_ChatRoom_Chat_Video
from ui_chatroom_chat_voice import Ui
