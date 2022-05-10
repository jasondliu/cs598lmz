import socket
import time
from threading import Thread

from ethereum import slogging
from rlp.utils import decode_hex
from ethereum.utils import encode_hex, sha3
from ethereum.slogging import get_logger
from ethereum.transactions import Transaction
from ethereum.utils import encode_hex, decode_hex
from ethereum.keys import privtoaddr
from ethereum.state import State
from ethereum.block import Block
from ethereum.blocks import BlockHeader
from ethereum.processblock import apply_transaction
from devp2p.service import WiredService, WiredClient
from devp2p.protocol import BaseProtocol
from devp2p.app import BaseApp
from devp2p.utils import host_port_pubkey_to_uri
from devp2p.discovery import NodeDiscovery

from raiden import messages
from raiden.network.transport import UDPTransport
from raiden.messages import decode, encode

log = get_logger('raiden.network.discovery')


class DiscoveryProtocol(BaseProtocol):

