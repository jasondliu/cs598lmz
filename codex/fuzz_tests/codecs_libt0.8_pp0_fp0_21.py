import codecs
codecs.register(idna.register)
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtNetwork

class Server(QObject):
    def __init__(self, Server_IPv4, Server_Port, Server_Domain, Protocol, Parent=None):
        super(Server, self).__init__(Parent)
        self.Parent = Parent
        self.Server_IPv4 = Server_IPv4
        self.Server_Port = Server_Port
        self.Server_Domain = Server_Domain
        self.Protocol = Protocol
        if self.Protocol == 'TCP':
            self.Server = QtNetwork.QTcpServer(self)
            self.Server.newConnection.connect(self.Connect)
        elif self.Protocol == 'UDP':
            self.Server = QtNetwork.QUdpSocket(self)
            self.Server.readyRead.connect(self.
