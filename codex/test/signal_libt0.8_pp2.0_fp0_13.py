import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gtk, psutil
from os.path import join, dirname 

from sugar.activity import activity
from sugar.datastore import datastore
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.graphics.toolbutton import ToolButton
from sugar.activity.widgets import ActivityToolbarButton
from sugar.activity.widgets import StopButton
from sugar.activity.widgets import TitleEntry

import webkit
from webkit import WebView

from gettext import gettext as _


class WebBrowser_Activity(activity.Activity):

    def __init__(self, handle):
        super(WebBrowser_Activity, self).__init__(handle)

        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
