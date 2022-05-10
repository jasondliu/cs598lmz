import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, GObject, Gio, Gdk
from menu_bar_applet import MenuBarApplet

from blueman.main.Config import Config


class TrayPopupMenu(Gtk.Menu):
    __gsignals__ = {
        'show': 'override',
        'popup-menu': 'override',
        'popdown-menu': 'override'
    }

    def __init__(self, plugin):
        GObject.GObject.__init__(self)

        self.plugin = plugin
        self.props.reserve_toggle_size = False
        self.connect("notify::visible", self.on_visible_toggled)

        self.down = False

        visible = Config("org.blueman.plugins.applet").get("visibility")
