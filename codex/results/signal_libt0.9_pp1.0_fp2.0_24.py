import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import gtk

application = gtk.icon_theme_get_default()
data_dir = os.path.dirname(__file__)
data_dir = os.path.join(data_dir, "..", "..", "..", "data")
data_dir = os.path.abspath(data_dir)
application.prepend_search_path(data_dir)

import UI.View as view
import UI.Controller as controller
import Model.Configuration as configuration
import BH.BH as game

class Main:
    def __init__(self):
        self.configuration = configuration.Configuration()
        self.view = view.View()
        self.controller = controller.Controller(self.configuration, self.view)
        self.win = self.view.create_window()
        self.game_thread = None
        self.win.connect('destroy', self.window_destroy)

        self.start_button = self.win.get_widget("play_button
