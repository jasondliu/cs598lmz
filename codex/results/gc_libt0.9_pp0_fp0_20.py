import gc, weakref
import time

import numpy as np

#______________________________________________________________________________
def objgraph_by_name(name, short=True):
    '''
    Show a graph of above-average objects by name.
    '''
    gc.collect()

    wcount = {}
    wref = {}
    duplicate_count = 0
    for wr in gc.get_referrers(gc.get_objects()):
        if isinstance(wr, weakref.ReferenceType):
            ob = wr()
            if ob is None:
                continue
            obid = id(ob)
            wref[obid] = wr
            wcount[obid] = wcount.get(obid, 0) + 1
            if wcount[obid] > 1:
                duplicate_count += 1

    total_ocs = len(wcount)

    print 'gc.get_objects():', len(gc.get_objects())
    print 'Duplicate objects:', duplicate_count
    print 'Unique objects:', len(wcount)

    longname = None
    shortname
