import mmap
from ipc_manager import IPCManager
from route_manager import RouteManager
from message_manager import MessageManager
from utils import *
import pdb
from corelib import logger
from corelib import log

DEFAULT_NETWORK = 'rocketfuel'
DEFAULT_BANDWIDTH = 10
DEFAULT_DELAY = 0
DEFAULT_BUFFER = 100

class CoreManager(object):
    '''
    manages a list of cores and the data paths between them
    '''

    def __init__(self, settings):
        '''
        loads the settings for this manager into a private dictionary
        '''

        self.logger = logger.getChild('CoreManager')
        self.core_count = None
        self.core_settings = None
        self.core_ipc_dict = {}
        self.core_file_dict = {}
        self.core_route_dict = {}
        self.core_name_dict = {}
        self.update_settings(settings)

    def update_settings(self, settings):
        '''
        updates settings
