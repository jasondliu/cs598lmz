fn = lambda: None
# Test fn.__code__; this will fail if fn is too old, e.g. name
# mangling is missing.
fn.__code__


test_largefile_support.addSuccess(LargefileTest, sys.argv[0],
                                  test.test_largefile)


def test_main():
    test.test_support.run_unittest(test_largefile_support)


if __name__ == "__main__":
    test_main()
