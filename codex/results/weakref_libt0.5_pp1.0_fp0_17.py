import weakref

from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol
from twisted.python import log

from txtorcon import TorControlProtocol, TorProtocolFactory
from txtorcon import TorState, build_tor_connection
from txtorcon import TorConfig, TCPHiddenServiceEndpoint, TorNotFound
from txtorcon import DEFAULT_VALUE
from txtorcon.interface import ITorControlProtocol
from txtorcon.util import find_keywords
from txtorcon.util import find_tor_binary
from txtorcon.util import is_valid_port
from txtorcon.util import available_tcp_port
from txtorcon.util import expand_file
from txtorcon.util import is_onion_address
from txtorcon.util import join_socks_host_port
from txtorcon.util import join_host_port
from txtorcon.util import split_socks_host_port
from txtorcon.util import split_host_port
from txtor
