import weakref
from Qt import QtCore, QtGui, QtWidgets, _loadUi

from avalon import api, maya, io
from avalon.maya.lib import colorfunctions
from avalon.tools import lib as toolsLib
from avalon.vendor import qtawesome


# module level
dialog = None
actions = []
seen_assets = list()
dialog_instance = None

# Fonts
FONT_BOLD = QtGui.QFont()
FONT_BOLD.setBold(True)


def get_unique_assets(data):
    """
    Get the unique asset for each asset
    :param data: asset_id and instances
    {'asset_id': [
        {'asset': 'Character_Junior_01', 'name': 'jnr01_Grp_001'},
        {'asset': 'Character_Junior_01', 'name': 'jnr01_Grp_002'},
        {'asset': 'Character_Junior_01', 'name': 'jnr01_Grp
