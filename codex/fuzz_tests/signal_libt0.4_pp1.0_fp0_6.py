import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap

from ui_mainwindow import Ui_MainWindow
from ui_settings import Ui_Settings
from ui_about import Ui_About
from ui_log import Ui_Log
from ui_calendar import Ui_Calendar
from ui_calendar_event import Ui_CalendarEvent
from ui_calendar_event_edit import Ui_CalendarEventEdit
from ui_calendar_event_view import Ui_CalendarEventView
from ui_calendar_event_delete import Ui_CalendarEventDelete
from ui_calendar_event_invite import Ui_CalendarEventInvite
from ui_calendar_event_
