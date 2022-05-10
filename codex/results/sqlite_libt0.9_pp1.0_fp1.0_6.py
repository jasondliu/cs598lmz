import ctypes
import ctypes.util
import threading
import sqlite3
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from datetime import datetime
from io import StringIO
from urllib.parse import urlparse
from PIL import Image
import os
from web3 import Web3
from time import sleep

from ui import sync_data_worker, sync_account_data, Main, WaitDialog
from eth_wallet import ETHWallet
from eth_wallet import rpc, collect_wallets, get_wallet_data, get_wallet_nonce, get_wallet_gaslimit
import colors as colors_

from utils.logger import init_logger
from utils.signals import Signals

from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject, GLib, Pango, Gio
from gi.repository.GdkPixbuf import Pixbuf
from gi.repository.Gtk import SizeGroup

from lib.bitcoin import (
