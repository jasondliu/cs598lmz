import weakref

from Qt import QtWidgets, QtGui, QtCore
from maya import OpenMayaUI as omui

from zoo import zapi
from zoo.libs.pyqt import utils
from zoo.libs.pyqt.extended import combobox
from zoo.libs.pyqt.widgets import layouts, extended
from zoo.libs.pyqt.widgets.frameless import FramelessWindow
from zoo.libs.zooscene import zoosceneconstants as const
from zoo.libs.zooscene import zooscenefiles
from zoo.libs.zooscene.constants import ZOOSCENE_CONTEXT

from zoo.preferences.core import preference
from zoo.preferences.gui import preferencesgui

from zoo.libs.utils import zlogging

logger = zlogging.getLogger(__name__)


def mayaToQT(name):
    """
    Maya -> QWidget

    :param name: Maya UI name to convert
    :type name: str
    :return:
