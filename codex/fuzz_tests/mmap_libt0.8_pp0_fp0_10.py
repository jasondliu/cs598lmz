import mmap
import binascii
import sys

def reverse_bytes(s):
    return s[::-1]

#header_sizes_rom = {"SNES":0x200, "NES":0x10, "GB":0x100, "GBA":0x200, "GBC":0x100}

#for_header = {"SFC":0x200, "SMC":0x200, "SMC":0x200, "GB":0x100, "GBC":0x100}

#def get_INFO(rom, force_type=None):
def get_INFO(rom, force_type=None, verbose=None):

    #types = ["SFC", "SMC", "SMC", "GB", "GBC"]

    #if force_type == None:
    #    type_ = types[random.randrange(0, len(types))]
    #else:
    #    type_ = force_type

    #header_size = header_sizes_rom[type_]
    #header_size = 0x200

   
