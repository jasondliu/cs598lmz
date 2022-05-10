import socket
import threading
import time

import paramiko

from utils import logger, ssh_utils


class SSHClient:

    def __init__(self, host, port, username, password, timeout=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.transport = None
        self.sftp = None
        self.channel = None

    def connect(self):
        self.client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password,
                            timeout=self.timeout)
        self.transport = self.client.get_transport()
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

