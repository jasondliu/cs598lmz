import _struct
import _thread
import argparse

from trezor import log, wire
from trezor.messages import InputScriptType

from apps.common.debug import DebugOutput
from apps.common.seed import Keychain

PROTOCOL_VERSION = 4

brick_name = "Trezor"

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
