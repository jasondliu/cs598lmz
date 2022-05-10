import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import pickle

from PyQt5.QtCore import Qt, QTimer, QThread, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QLabel, QSizePolicy, QVBoxLayout, QHBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsPixmapItem, QGraphicsTextItem, QGraphicsLineItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsPathItem, QGraphicsPolygonItem, QGraphicsSimpleTextItem, QGraphicsItemGroup, QGraphicsAnchorLayout, QGraphicsAnchor, QGraphicsGridLayout, QGraphicsLinearLayout, QGraphicsLayoutItem, QGraphicsWidget, QGraphicsProxyWidget, QGraphicsBlurEffect, QGraphicsDropShadowEffect, QGraphicsColorizeEffect, QGraphicsOpacityEffect, QGraphicsEffect, QGraphicsSceneMouseEvent, QStyleOptionGraphicsItem, QGraphicsSceneHoverEvent, QGraphicsSceneContextMenuEvent, QGraphicsSceneHelpEvent,
