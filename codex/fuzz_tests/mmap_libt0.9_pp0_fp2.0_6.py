import mmap

from elftools.elf.elffile import ELFFile

import exec_analyser
 

def display_help():
	print("""
-----------------------------------------------------------------
Usage: {} <ELF_file>

Remark: it will generate a log file containing all the addresses
-----------------------------------------------------------------
""".format(__file__))
	
def add_unknown_address(a, my_map_unknown_addresses):
	if a in my_map_unknown_addresses.keys():
		my_map_unknown_addresses[a] += 1
	else:
		my_map_unknown_addresses[a] = 1


def print_info_screen(clock_title, t1):
	print("\n{} - {:.3f}s".format(clock_title, t1))

def compute_all_bytes(a_mem_section, nb_bytes, my_mmap_file, my_map_all_bytes):
	for i in range(nb_bytes):
		abs_addr = a_mem_section.header['sh_addr
