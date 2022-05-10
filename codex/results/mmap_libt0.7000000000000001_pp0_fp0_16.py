import mmap
import struct
import traceback

from . import debug
from . import utils
from .hccap import Hccap
from .hccapx import Hccapx
from .pcapng import Pcapng
from .wepkey import Wepkey
from .wpa_decrypt import WPA_Decrypt


class Wpa2Decrypt(object):
    def __init__(self, hccap, hccapx, wepkey, pcapng, wpa_decrypt, capfile):
        self.capfile = capfile
        self.hccap = hccap
        self.hccapx = hccapx
        self.wepkey = wepkey
        self.pcapng = pcapng
        self.wpa_decrypt = wpa_decrypt
        self.timestamp = int(time())

    def __indent__(self, level):
        return '  ' * level

    def __parse_radiotap__(self, radiotap):
        """
        Parse radiotap header
        """
       
