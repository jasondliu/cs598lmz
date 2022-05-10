import weakref
from functools import partial
import sublime_plugin


class SyncSettings(sublime_plugin.EventListener):

    """
    Sync settings across view via custom event and weakref.
    """

    def on_load(self, view):
        if getattr(view, 'is_widget', False):
            return
        self.sync(view)

        # update sync settings on view change, so that new views are added to
        # all synced views.
        view.settings().add_on_change('settings_sync', partial(self.sync, view))

    def sync(self, view):
        """
        Sync settings across all synced views.

        The original view is stored as a weak reference so that the callback
        for the settings changes does not produce a reference cycle.
        """
        # get all synced views from the original view
        synced_views = view.settings().get('settings_sync.views', [])

        # get a weak reference to the original view
        weak_view = weakref.ref(view)

        # store the view along with the weak reference in the settings
