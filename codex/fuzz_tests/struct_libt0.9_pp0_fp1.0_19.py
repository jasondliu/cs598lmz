import _struct
import ida_idaapi
import ida_idc
import ida_kernwin
import ida_lines
import ida_loader
import ida_pro
import ida_segment
import ida_bytes
import ida_auto
import ida_funcs
import ida_nalt
import ida_nlist
import ida_range
import ida_segregs
import ida_struct
import ida_typeinf
import ida_idp
import ida_diskio
import ida_entry
import ida_fixup
import ida_frame
import ida_gdl
import ida_graph
import ida_netnode
import ida_name
import ida_range
import ida_search
import ida_typeinf
import ida_kernwin
import ida_bytes
import ida_pro
import ida_ida

class IDAWrapper(object):
    def __init__(self, addr):
        self.addr = addr

    def __getattr__(self, name):
        fn =
