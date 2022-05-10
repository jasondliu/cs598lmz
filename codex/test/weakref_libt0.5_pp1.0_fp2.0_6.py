import weakref

import numpy as np

from qtpy import QtWidgets, QtCore

from glue.config import viewer_tool
from glue.core.subset import RoiSubsetState
from glue.utils.qt import load_ui
from glue.viewers.common.qt.tool import CheckableTool
from glue.viewers.common.qt.toolbar import GlueToolbar


__all__ = ['CursorTool', 'CursorToolbar']


class CursorTool(CheckableTool):

    icon = 'glue_crosshair'
    tool_id = 'cursor'
    action_text = 'Toggle cursor'
    tool_tip = 'Toggle cursor'
    status_tip = 'Toggle cursor'

    def __init__(self, viewer):

        super(CursorTool, self).__init__(viewer)

        self.mode = 'select'

        self._cursor_mode_action = QtWidgets.QAction(self)
        self._cursor_mode_action.setText('Cursor Mode')
        self._cursor_
