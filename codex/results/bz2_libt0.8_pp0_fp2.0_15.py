import bz2
bz2.MAX_WBITS = 0
import sys, json
from collections import OrderedDict

if len(sys.argv) > 1:
    files = sys.argv[1:]
else:
    print "usage:", sys.argv[0], "file0 [ file1 file2 ... ]"
    sys.exit(0)

def find_parent(moves, loc, depth=0):
    if depth > 10:
        return None
    for m in moves:
        if m['loc'] == loc:
            return m
        if 'moves' in m:
            parent = find_parent(m['moves'], loc, depth+1)
            if parent is not None:
                return parent
    return None

for f in files:
    with bz2.BZ2File(f, 'r') as data:
        json_data = json.loads(data.read())
        for game in json_data:
            moves = []
            for k, move in enumerate(game['moves'], start=1):
                x = move
