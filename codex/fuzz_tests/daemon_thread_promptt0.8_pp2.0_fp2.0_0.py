import threading
# Test threading daemon
import multiprocessing

#debug = True
debug = False


def get_widget_by_path(widget, path):
    """
    Get a widget based on it's path, like in GtkBuilder
    :param widget: GtkWidget to search in
    :param path: GtkWidget path
    :returns: GtkWidget
    """

    if widget is None:
        return None
    if path is None:
        return None
    if path is '':
        return widget

    path_splitted = path.split('/')
    if path_splitted[0] == widget.get_name():
        return get_widget_by_path(widget, "/".join(path_splitted[1:]))
    else:
        return None

class GUI_Wrapper(Gtk.Builder):
    def __init__(self, gui_file, glade_path):
        logger.debug("Wrapper init")
        Gtk.Builder.__init__(self)
        self.add_from_file(gui_file)
        self.add_from_
