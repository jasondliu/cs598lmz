import threading
threading.stack_size(256 * 1024 * 1024)

from collections import deque

from cloudshell.shell.core.session.cloudshell_session import CloudShellSessionContext
from cloudshell.shell.core.driver_context import ResourceCommandContext, ResourceContextDetails, ReservationContextDetails, ConnectivityContext
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.driver_context import InitCommandContext, AutoLoadDetails, AutoLoadAttribute, AutoLoadResource, AutoLoadDetailsUpdated
from data_model import *  # run 'shellfoundry generate' to generate data model classes
from cloudshell.api.cloudshell_api import CloudShellAPISession
#from cloudshell.shell.core.driver_utils import GlobalLock
from cloudshell.core.logger import qs_logger
import json

from cloudshell.traffic.tg_helper import get_reservation_resources, get_family_attribute, get_family_attribute_value
from cloudshell.traffic.tg_helper import get_all_ports
from cloudshell.traffic.tg_helper
