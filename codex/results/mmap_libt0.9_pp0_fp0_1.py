import mmap
from tinylist import tlist
import pefile

from miasm2.analysis.machine import Machine
from miasm2.os_dep.win_api_x86_32 import win_api_x86_32
from miasm2.jitter.csts import PAGE_READ, PAGE_WRITE

PE_TYPE = {pefile.PE_TYPE['PE32']:"PE x86 32 bits",
           pefile.PE_TYPE['PE32+']:"PE x64 64 bits"}



def parse_args():
    "Parse arguments"

    parser = argparse.ArgumentParser(description="ELF Binaries Analyzer")
    parser.add_argument('filename', help="File to analyze")

    args = parser.parse_args()
    return args.filename



def exec_pe(filename):
    "Execute a PE file in memory"
    print 'Launching PE file: %s' % filename

    # Init Maima machine
    machine = Machine('x86_32')
    mn, dis_engine = machine.mn, machine.dis_engine
