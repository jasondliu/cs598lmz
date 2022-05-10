import ctypes
import ctypes.util
import threading
import sqlite3

class DbusInterface(object):
  def __init__(self, bus_name, object_path, interface_name, retry_count=10, retry_interval=0.1):
    self.bus_name = bus_name
    self.object_path = object_path
    self.interface_name = interface_name
    self.retry_count = retry_count
    self.retry_interval = retry_interval
    self.bus = dbus.SessionBus()
    self.proxy = None
    self.proxy = self.create_proxy()
    self.proxy.connect_to_signal("Changed", self.on_changed)

  def create_proxy(self):
    for i in range(self.retry_count):
      try:
        return self.bus.get_object(self.bus_name, self.object_path)
      except dbus.exceptions.DBusException as e:
        time.sleep(self.retry_interval)
    raise e

  def on_changed(self):
    self
