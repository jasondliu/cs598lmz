import socket
import threading
import time
from typing import Dict

from gi.repository import GObject

from blueman.Functions import dprint, get_icon
from blueman.bluez.Adapter import Adapter
from blueman.bluez.Device import Device
from blueman.main.Config import Config
from blueman.plugins.ManagerPlugin import ManagerPlugin
from blueman.main.AppletService import AppletService

from blueman.Sdp import *


class DeviceList(ManagerPlugin):
    __depends__ = ["StatusIcon", "Menu"]
    __icon__ = "blueman-devices"
    __author__ = "Walmis"
    __description__ = _("Provides a list of discovered bluetooth devices")
    __priority__ = 3

    def on_load(self) -> None:
        # type: () -> None

        self.devices: Dict[str, Device] = {}
        self.handlers = []

        self.handlers.append(self.Manager.connect("adapter-removed", self.on_adapter_removed))

       
