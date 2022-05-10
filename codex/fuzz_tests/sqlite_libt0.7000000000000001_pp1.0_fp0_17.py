import ctypes
import ctypes.util
import threading
import sqlite3
import json
from datetime import datetime

from twisted.web import server
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet.defer import Deferred
from twisted.web.server import NOT_DONE_YET

from txircd.modbase import Mode, Command
from txircd.server import ServerFactory
from txircd.utils import ircLower
from txircd.modules.xlinebase import XLineBase
from txircd.modules.servprotectbase import ServProtectBase
from txircd.modules.servprotectbase import checkAccess
from txircd.modules.servprotectbase import checkPermission
from txircd.modules.servprotectbase import checkPermissionWithTarget
from txircd.modules.servprotectbase import checkPermissionWithChannel

class WebIRC(XLineBase, ServProtectBase):
    def hookIRCd(self, ircd):
        self.ircd = ircd
        self.ircd.server
