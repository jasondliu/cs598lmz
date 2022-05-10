import weakref

from PyQt5.QtCore import QObject, QDateTime, QCoreApplication, QTimer, QEventLoop
from PyQt5.QtDBus import QDBusConnection, QDBusPendingCall, QDBusMessage, QDBusInterface, QDBusAbstractInterface

from . import log

class DBusInterfaceBase(QObject):
	def __init__(self, bus, path, interface):
		super().__init__()
		self._bus = bus
		self._path = path
		self._interface = interface
		self._iface = QDBusInterface(self._bus, self._path, self._interface)
		self._iface.setTimeout(5000)
		self._iface.connection().connect(self._bus, self._path, self._interface, 'PropertiesChanged', self.on_properties_changed)
		self._iface.connection().connect(self._bus, self._path, self._interface, 'InterfacesAdded', self.on_interfaces_added)
		self._iface.connection
