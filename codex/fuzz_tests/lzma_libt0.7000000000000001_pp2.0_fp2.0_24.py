import lzma
lzma.open
import os
import functools

from . import unix2windows
from . import windows2unix

def report_error(message, filename, lineno):
    print('{}: {}:{}: {}'.format(
        os.path.basename(sys.argv[0]),
        filename,
        lineno,
        message
    ))

def main():
    parser = argparse.ArgumentParser(description='Convert from unix to windows line endings')
    parser.add_argument('files', metavar='N', type=str, nargs='*',
                        help='File to convert.')
    parser.add_argument('--output', type=str,
                        help='Output file. Defaults to the same file')
    parser.add_argument('--windows2unix', action='store_true',
                        help='Convert windows to unix line endings')
    parser.add_argument('--unix2windows', action='store_true',
                        help='Convert unix to windows line endings')
    args = parser.parse_args()

   
