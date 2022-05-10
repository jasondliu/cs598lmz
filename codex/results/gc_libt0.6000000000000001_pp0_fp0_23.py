import gc, weakref

import gevent

from . import (
    log,
    )
from .plugin import (
    Plugin,
    )


class PluginManager(object):
    """
    """

    def __init__(self):
        self._plugins = []
        self._plugins_by_name = {}
        self._plugins_by_class = {}

    def load_plugins(self):
        # import all plugins
        import gevent_openssh.plugin
        self._plugins.extend(gevent_openssh.plugin.load_plugins())
        # import all user-supplied plugins
        import gevent_openssh.plugin.user
        self._plugins.extend(gevent_openssh.plugin.user.load_plugins())

    def initialize_plugins(self):
        for plugin in self._plugins:
            self._plugins_by_name[plugin.__name__] = plugin
            self._plugins_by_class[plugin] = plugin
            plugin.initialize()

    def get_plugin(self, name):
        return self._plugins_by_name.get(
