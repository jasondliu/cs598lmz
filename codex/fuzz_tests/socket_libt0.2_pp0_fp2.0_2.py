import socket
import sys
import time
import os
import threading

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_mainwindow import Ui_MainWindow
from ui_dialog_login import Ui_Dialog_login
from ui_dialog_register import Ui_Dialog_register
from ui_dialog_chat import Ui_Dialog_chat
from ui_dialog_add_friend import Ui_Dialog_add_friend
from ui_dialog_add_group import Ui_Dialog_add_group
from ui_dialog_add_group_member import Ui_Dialog_add_group_member
from ui_dialog_group_chat import Ui_Dialog_group_chat
from ui_dialog_group_member import Ui_Dialog_group_member
from ui_dialog_group_setting import Ui_Dialog_group_setting
from ui_dialog_friend_setting import Ui_Dialog
