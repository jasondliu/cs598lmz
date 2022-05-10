import signal
signal.signal(signal.SIGINT, signal_handler)

import kpp

result = subprocess.run(["pgrep", "kpp"], stdout=subprocess.PIPE)
assert result.stdout

import time

from kpp import KeyPress

from evdev import list_devices, InputDevice
from select import select

from colors import colors
from colors import colors_2

from printer import Printer
from printer import PrinterLogged

from logfile import Logfile

from dynamic import Dynamic
from dynamic import DynamicClosed

from slider import Slider
from slider import Slider4
from slider import Slider4B
from slider import SliderComposed

from binary import Binary
from binary import BinaryLogged

from binary_simple import BinarySimple
from binary_simple import BinarySimpleLogged

from binary_simple_v2 import BinarySimpleV2
from binary_simple_v2 import BinarySimpleV2Logged
from binary_simple_v2 import BinarySimpleV2Closed
from binary_simple_v2 import BinarySimpleV2ClosedLogged

