import sys, threading
threading.Thread(target=lambda: sys.stderr.write(__file__.upper() + '\n')).start()

"""
FASTA file reader and writer
"""

from ..externals.six import print_

