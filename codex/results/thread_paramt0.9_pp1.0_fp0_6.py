import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n')).start()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import os, sys, urllib, json
import filecmp, datetime, time
from multiprocessing import Pool, cpu_count
from optparse import OptionParser

p = OptionParser()
p.add_option('--target', '-t', type=str)
p.add_option('--background', '-b', action="store_true", default=False,
             help="execute in the background (requires python-daemon)")
p.add_option('--daemonize', '-d', action="store_true", default=False,
             help="execute in the background (requires python-daemon)")
p.add_option('--interval', '-i', type="float", default=5.0,
             help="interval between checks in seconds (default: 5)")
p.add_option('--max_buff', '-m', type="int", default=256,
             help="warn when buffer exceeds
