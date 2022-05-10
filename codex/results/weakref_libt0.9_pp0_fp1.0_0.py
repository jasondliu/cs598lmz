import weakref
import collections
import socket

# openaps imports
import openaps
import openaps.cli.subcommand
import openaps.configurable
from openaps.cli.commandmap import CommandMap
import openaps.config

from openaps.device.monitor import MonitorBase

class MonitorDevice(object):
  commands = CommandMap( )
  def __init__ (self, device):
    self.device = device
    self.app = device.app
    self.driver = self.config = None
    self.discover( )
  def discover (self):
    self.config = self.config_class(self.device.name, self.app.config)
    self.driver = self.config.get_device(self.device.name)
  @property
  def config_dir (self):
    return 'monitor'
  @property
  def config_class (self):
    return self.app.config.get_device_class(self.config_dir)
  @property
  def record (self):
    return self.config.get_record(self.config_dir
