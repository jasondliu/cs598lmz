import gc, weakref
from gi.repository import Gtk, GObject, Gdk, GLib
from object_handling import ObjectHandling, MenuType

@Gtk.Template(resource_path='/org/gnome/GnomeSetting/mainwindow.ui')
class MyApplication(Gtk.ApplicationWindow, ObjectHandling):
    __gtype_name__ = 'MyApplication'

    def __init__(self, object_model, object_view, object_controller, *rest):

        Gtk.ApplicationWindow.__init__(self)
        self.init_template()
        ObjectHandling.__init__(self, object_model, object_view, object_controller)

        self.set_title(self.controller.APP_TITLE)
        self.set_default_size(self.controller.APP_SIZE_X, self.controller.APP_SIZE_Y)
        self.set_default_icon_from_file(self.controller.APP_ICON)

        self.set_resizable(self.controller.APP_RESIZABLE)
        self.set_position
