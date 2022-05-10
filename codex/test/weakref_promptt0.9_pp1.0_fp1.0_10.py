import weakref
# Test weakref.ref
with tvm.build_config(auto_unroll_max_step=1):
    mincrtmp = tvm.placeholder((2,), dtype="float32")
    mincr = tvm.compute((2,), lambda x: mincrtmp[x] + 5, name="mincr")
    m = tvm.build(mincr, [mincrtmp])


def verify_ref(ref):
    assert ref.value == 5
    del ref
    try:
        ref.value
        print("Cannot go here")
    except Exception as e:
        print("Test WeakRef pass")

ref = weakref.ref(m)
verify_ref(ref)

if __name__ == "__main__":
    unittest.main()
