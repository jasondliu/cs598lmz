import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()

from pymol import cmd, stored, util

while True:
    cmd.set_bond(stored.order, 'hb2', 'hb1', 1.5)  # pkaa-4412
    cmd.set_bond(stored.order, 'hb3', 'hb1', 1.5)  # pkaa-4411
    util.mroll(stored.sele1, 60, 0, 0)
    cmd.refresh()
