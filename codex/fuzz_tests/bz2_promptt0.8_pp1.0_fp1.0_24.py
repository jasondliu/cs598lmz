import bz2
# Test BZ2Decompressor because that is the one that is used by any
# 'bz2' compression handler
test_support.run_unittest(
    BZ2DecompressorTests,
    DeprecationTests,
)

if __name__ == "__main__":
    test_main()
