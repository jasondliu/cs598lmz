import weakref

from PyQt5.QtCore import Qt, QPointF, QRectF, QRect, QTimer
from PyQt5.QtGui import QColor, QBrush, QPen, QPainterPath, QPainter, QFont, QFontMetrics
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsSimpleTextItem, QGraphicsItemGroup, QGraphicsProxyWidget

from urh.controller.dialogs.ModulatorDialog import ModulatorDialog
from urh.controller.dialogs.TransmitterDialog import TransmitterDialog
from urh.dev.BackendHandler import BackendHandler
from urh.dev.native.Device import Device
from urh.dev.VirtualDevice import Mode, VirtualDevice
from urh.signalprocessing.Message import Message
from urh.signalprocessing.Participant import Participant
from urh.signalprocessing.ProtocolAnalyzer import ProtocolAnalyzer
from urh.signalprocessing.ProtocolGroup import ProtocolGroup
from urh.util.Logger import logger
from urh.util.SettingsProxy import
