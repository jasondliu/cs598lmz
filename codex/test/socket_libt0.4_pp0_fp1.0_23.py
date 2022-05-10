import socket
import threading
import time

from sqlalchemy import and_

from common.constants import *
from common.logger import Logger
from common.utils import *
from db.models import *
from db.session import Session
from modules.module import Module
from modules.module_manager import ModuleManager
from modules.module_result import ModuleResult

class Network(Module):

    def __init__(self):
        self.name = "Network"
        self.description = "Network module"
        self.threads = []
        self.logger = Logger()

    def run(self, session, options):
        self.logger.log("[*] Starting Network module")
        self.logger.log("    [*] Getting network information")
        self.get_network_info(session)
        self.logger.log("    [*] Getting network connections")
        self.get_network_connections(session)
        self.logger.log("    [*] Getting network interfaces")
        self.get_network_interfaces(session)
