import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a))
lst.append(weakref.ref(a,callback))
"""
    from numba import bytecode
    from numba.analysis import compute_cfg_from_blocks
    from numba.analysis import compute_use_defs
    from numba.analysis import compute_live_map
    from numba.analysis import compute_reaching_definitions
    from pprint import pprint
    bc = bytecode.ByteCode(src)
    cfg = compute_cfg_from_blocks(bc.blocks)
    bc.show()
    cfg.show()
    ud = compute_use_defs(cfg)
    pprint(ud)
    lm = compute_live_map(cfg, ud)
    pprint(lm)
    # TODO: Add an assert to make sure that the live map is correct:
    #
    # self.assertTrue(bc.blocks[4].liveout == frozenset(['c']))
    #
    rd = compute_reaching_definitions(
