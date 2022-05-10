import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:", check_same_thread=False)

def _(x):
    return x

class Plugin:
    """
    Base class for plugins.
    """
    def __init__(self, app, name):
        self.name = name
        self.app = app
        self.actions = []
        self.db = None

    def get_actions(self):
        """
        Returns a list of actions to be registered.
        """
        return self.actions

    def get_db(self):
        """
        Returns a database (sqlite3) handle.
        """
        if not self.db:
            db_name = self.app.config.get_string('/apps/cinnamon/plugins/%s/db_name' % self.name)
            if db_name:
                self.db = sqlite3.connect(db_name, check_same_thread=False)
                self.db.row_factory = sqlite3.Row
            else:
                self.db = sqlite3.connect(":memory:", check_
