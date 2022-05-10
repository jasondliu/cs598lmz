import gc, weakref
import gtk

from plugins.engine import Plugin

from xl import event, providers, settings
from xl.nls import gettext as _
from xlgui import icons
from xlgui.widgets import menu, dialogs

class PlaylistManager(Plugin):
    """
        This plugin provides a playlist manager.
    """
    def enable(self):
        """
            Enables the plugin
        """
        self.playlist_manager = PlaylistManagerWindow(self.exaile.gui.main.window)
        self.playlist_manager.show()
        self.playlist_manager.connect('destroy', self.on_playlist_manager_destroy)
        
        providers.register('main-menu', menu.MenuItem('playlists', _('Playlists'), stock=gtk.STOCK_CONVERT))
        providers.register('main-menu-playlists', menu.simple_menu_item_factory('playlist_manager', _('Manage Playlists'), self.on_playlist_manager_activate))
        
        event.add_ui_callback(self
