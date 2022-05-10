import weakref
import time

from gi.repository import Gtk

from sugar3.activity.activity import Activity, ActivityToolbox
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity.widgets import DescriptionItem


class TicTacToeActivity(Activity):
    def __init__(self, handle):
        Activity.__init__(self, handle)

        self.max_participants = 1

        self.game = None
        self.build_toolbar()
        self.build_game()

        self.show_all()

    def build_toolbar(self):
        toolbar_box = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_
