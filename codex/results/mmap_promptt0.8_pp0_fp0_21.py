import mmap
# Test mmap.mmap with a non-existing file.
# Should raise ValueError on Unix, but Windows may return 0.
for fil in ('<A very unlikely file name for testing purpose>',
            '/dev/null/not'):
    try:
        mmap.mmap(0, 1, fil)
    except OSError as msg:
        pass
    except ValueError:
        pass
    else:
        print("test failed with filename: %s" % fil)
        # Break out of the loop as we've already proven that mmap works with
        # non-existing files.
        break
