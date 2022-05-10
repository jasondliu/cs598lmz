import bz2
# Test BZ2Decompressor.__init__()

def check_attr(attr, value=None):
    if value is not None:
        print("Testing %s == %s ..." % (attr, value), end="")
        if getattr(bz2, attr) != value:
            raise TestFailed("%s is %s, should be %s" %
                             (attr, getattr(bz2, attr), value))
    else:
        print("Testing %s is not None ..." % attr, end="")
        if getattr(bz2, attr) is None:
            raise TestFailed("%s is None" % attr)
    print("ok")

check_attr("BZ_RUN")
check_attr("BZ_FLUSH")
check_attr("BZ_FINISH")
check_attr("BZ_OK")
check_attr("BZ_RUN_OK")
check_attr("BZ_FLUSH_OK")
check_attr("BZ_FINISH_OK")
check_attr("BZ_STREAM_END")

