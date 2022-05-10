import gc, weakref
from time import time
from os import remove
from os.path import exists, join, dirname, normpath
from itertools import chain
from threading import Event
from hashlib import md5
from crypt.util import to_hex_bytes, from_hex_bytes
from crypt.diffiehellman import DiffieHellman
from crypt.comm import enctype, transport
from crypt.cipher import Cipher
from crypt.asymmetric import AsymmetricAlgorithm
from pippin.config import cfg, merge_dicts, WRITE_CONFIG
from pippin.util import LogMixin, is_bytes, is_str
from pippin.unittest.compat import MultiprocessingMixin, TimingMixin
from pippin.unittest.util import fill_random, save_random, cleanup_random
from pippin.unittest.fuzz import fuzz


class MockPipe:
    def __init__(self, reps):
        if not isinstance(reps, int):
            reps = 1
        self.reps = reps
        if self
