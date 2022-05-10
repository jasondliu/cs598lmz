import weakref
import threading

import DebugPrint

from Exceptions import *
from Expire import Expire
from Roles import Roles

class Scope(object, metaclass=abc.ABCMeta):
    '''
    Base object for the OpenPix modules.

    It defines the basis for agent communication and it provides a flexible
    and easy to use message routing system.
    '''

    def __init__(self, **kwargs):
        self.roles = Roles()
        self.agents = []
        self.expire = Expire()

        self.addr = kwargs.get('addr', None) # Communication address.

        self.busy = False # True if the scope is under processing
        self.busy_lock = threading.RLock() # Lock for busy variable

    def __str__(self):
        return self.addr

    def __contains__(self, agent):
        return agent in self.agents

    def __iter__(self):
        return iter(self.agents)

    def __repr__(self):
        return 'Scope(id
