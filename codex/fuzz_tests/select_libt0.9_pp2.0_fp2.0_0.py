import select
from collections import namedtuple
from . import JsonClient, ClientConfig
from . import ProxyConfig
from dns import resolver
from proxy import SocksServer, SocksServerConfig
from ssh import SshTransport, credentials, SshClient
from ssh.exceptions import SSHException
from .dns import SafeDNSResolver, ResolveError
from .utils import check_ip_in_network, FatalError
from .http import HttpProxy, HttpProxyConfig
from .blacklist import BlackList
import logging
from dfproxy.base import BaseConfig
from gevent.queue import Queue
from threading import Thread, Event
from typing import List, Optional, Tuple, Callable


ProxyPair = namedtuple('ProxyPair', ('socks_proxy', 'http_proxy'))


def _get_ip_port_from_netloc(netloc):
    if not netloc:
        return '', None
    netloc = netloc.split('@')[-1]
    netloc = netloc.split(':')
    if not netloc:
        return '',
