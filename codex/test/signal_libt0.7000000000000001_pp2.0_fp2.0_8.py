import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk, GObject, GLib, Gio, Gedit

from threading import Thread

from . import NodeJsDebuggerView, NodeJsDebuggerModel, NodeJsDebuggerBackend

class NodeJsDebuggerPlugin(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "NodeJsDebugger"
    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)
        self.debuggerView = None
        self.debuggerModel = None
        self.debuggerBackend = None
        self.backendThread = None

    def do_activate(self):
        self.debuggerView = NodeJsDebuggerView(self.window)
        self.debuggerModel = NodeJsDebuggerModel()
