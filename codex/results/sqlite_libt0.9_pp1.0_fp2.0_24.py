import ctypes
import ctypes.util
import threading
import sqlite3
from multiprocessing import Process

from Foundation import *
from AppKit import *
from ScriptingBridge import *

from alfred.modules.core.web_socket_server import WebSocketServer
from alfred.modules.core.config import Config
from alfred.modules.core.constants import BUNDLE_ID

from alfred.modules.core.devices import Manager as DeviceManager
from alfred.modules.core.triggers import Manager as TriggerManager
from alfred.modules.core.modules import Manager as ModuleManager
from alfred.modules.core.interfaces import Manager as InterfaceManager
from alfred.modules.core.events import Manager as EventManager
from alfred.modules.core.log import LogManager


def main():
    #load_objc_runtime()
    #load_nsbundle()

    load_dll('/System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio', 'CoreAudio')
    load_dll('/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit', 'IOKit')
    load_dll
