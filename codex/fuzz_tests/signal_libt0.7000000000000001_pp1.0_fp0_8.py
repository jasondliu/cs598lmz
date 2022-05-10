import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import logging
from gi.repository import Gtk, Gdk
from xpra.platform import program_context
from xpra.gtk_common.quit import gtk_main_quit_really
from xpra.gtk_common.gtk_util import add_close_accel
from xpra.gtk_common.gobject_compat import register_os_signals
from xpra.client.gtk_base.gtk_client_base import GTKXpraClient


class XpraClient(GTKXpraClient):

    def __init__(self):
        GTKXpraClient.__init__(self)

    def client_type(self):
        return "Python/GTK3"

    def client_toolkit(self):
        return "gtk3"

    def build_info(self):
        info = GTKXpraClient.build_info(self)
        info.update({
            "version" : Gtk.get_major
