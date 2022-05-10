import threading
threading.main_thread().setName("MAIN")

from tornado.escape import json_decode, json_encode
from bson import json_util
from subprocess import call

from www.handlers.base import ProtectedRequestHandler, PublicRequestHandler
from www.beans import graphs
from www.lib.database import db
from configuration_global.logger_factory import LoggerFactory

from configuration_global.config_reader import ConfigReader


logger = LoggerFactory.create_logger(__name__)


# ######################################################################################################################
# ###################################################### GRAPH ########################################################
# ######################################################################################################################


class GraphHandler(ProtectedRequestHandler):

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

    async def get(self, action):
        action = action.lower()
        #
        if action == 'get':
            await self.get_graph()
        elif action == 'create':
            await self.create_graph()

