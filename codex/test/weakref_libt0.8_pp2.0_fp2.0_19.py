import weakref
import platform
import os
import pdb

from appserver.utils import create_app_factory

from appserver.plugins.tornado_plugin.application.tornado_application import TornadoMDS
from appserver.plugins.tornado_plugin.application.tornado_application import TornadoApplication

from appserver.plugins.tornado_plugin.model.tornado_mds_model import TornadoMDSModel

from appserver.plugins.tornado_plugin.controller.tornado_webserver import TornadoWebServer

from appserver.plugins.tornado_plugin.configurator.tornado_configurator import TornadoConfigurator

from appserver.plugins.tornado_plugin.utils.simple_tornado_logger import SimpleTornadoLogger

from appserver.plugins.tornado_plugin.utils.tornado_utils import get_mds_ip

class TornadoPlugin(object):

    def __init__(self, appserver_plugin_manager):

        self.appserver_plugin_manager = appserver_plugin_manager

