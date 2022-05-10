import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import llvm.core as lc
import llvm.passes as lp
import llvm.ee as le

def test():
    a = lc.Type.int()
    b = lc.Type.int()
    fnty = lc.Type.function(a, [b])
    fn = lc.Function.new(fnty, 'foo')

    bb = fn.append_basic_block('entry')
    bldr = lc.Builder.new(bb)
    tmp = bldr.add(fn.args[0], fn.args[0], "tmp")
    bldr.ret(tmp)

    pmb = lp.build_pass_managers(opt=3, loop_vectorize=True, loop_unroll=True)
    pmb.run(fn)
    print fn
    ee = le.Exec
