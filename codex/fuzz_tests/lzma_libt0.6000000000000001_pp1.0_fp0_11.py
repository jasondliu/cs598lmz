import lzma
lzma.open

from .utils import *

from .parsing import *
from . import parsing
from . import utils
from . import objects

from . import config
from .config import *

def main():
    parser = argparse.ArgumentParser(description='i3wm config manager',
                                     prog=__package__)
    parser.add_argument('-c', '--config', default=config.DEFAULT_CONFIG_PATH,
                        help='config path')
    parser.add_argument('-p', '--print-config', action='store_true',
                        help='print config')
    parser.add_argument('-l', '--list', action='store_true',
                        help='list configs')
    parser.add_argument('-i', '--install', action='store_true',
                        help='install config')
    parser.add_argument('-u', '--uninstall', action='store_true',
                        help='uninstall config')
    parser.add_argument('-r', '--restore', action='store_true',
                       
