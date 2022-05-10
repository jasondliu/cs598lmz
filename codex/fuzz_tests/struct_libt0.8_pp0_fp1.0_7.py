import _struct as struct

import os
import sys

boxes = {
    'subs': 0x0,
    'subs_c': 0x10,
    'subs_s': 0x11,
    'subs_en': 0x12,
    'subs_fr': 0x13,
    'subs_ru': 0x14
}

def parse_sub_info(sub_entry_path):
    rdata = open(sub_entry_path, 'r').read()

    #
    pos = 0
    idx = 0

    #
    out_subs_list = []

    while pos < len(rdata):
        entry_header,  = struct.unpack('>I', rdata[pos : pos + 4])

        start_pos = pos
        end_pos   = 0

        #
        sub_box_type,  = struct.unpack('>H', rdata[pos + 4 : pos + 6])
        sub_box_flags, = struct.unpack('>H', rdata[pos + 6 : pos + 8])
