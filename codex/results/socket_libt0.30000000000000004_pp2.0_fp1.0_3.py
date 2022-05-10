import socket
import sys
import threading
import time
import traceback
from multiprocessing import Process
from typing import List, Tuple

import pytest
from _pytest.monkeypatch import MonkeyPatch
from _pytest.tmpdir import TempdirFactory
from pytest_mock import MockFixture
from requests import Response
from requests.exceptions import ConnectionError

from rotkehlchen.assets.asset import Asset
from rotkehlchen.chain.ethereum.manager import NodeName
from rotkehlchen.chain.ethereum.sidechain_clients import (
    SidechainClient,
    SidechainClientFactory,
    SidechainClientType,
    SidechainClientTypeError,
    SidechainClients,
)
from rotkehlchen.chain.ethereum.sidechain_clients.bitcoin_sidechain_client import (
    BitcoinSidechainClient,
)
from rotkehlchen.chain.ethereum.sidechain_clients.litecoin_sidechain_client import (
    LitecoinSidechainClient,
)
from rotkehlchen.chain.et
