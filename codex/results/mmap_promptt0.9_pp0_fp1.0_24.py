import mmap
# Test mmap.mmap.move
def move_test():
    """Ensure that mmap.move works correctly.

    This test ensures that the mmap region is correctly updated after
    calling mmap.mmap.move and that out-of-bounds errors are correctly
    raised.
    """

    filename, storage_size = create_file()

    for dest in (0, 1, 2, 10, -2, -1):
        for src in (0, 1, 2, 10, -2, -1):
            for count in (0, 1, 2, 10, -2, -1):
                with mmap.mmap(open(filename), storage_size) as m:
                    # Out-of-bounds test.
                    try:
                        m.move(src, dest, count)
                    except ValueError:
                        pass
                    else:
                        if src < 0 or dest < 0 or count < 0 or src + count > storage_size or dest + count > storage_size:
                            raise Exception

                    if src >= 0 and dest >= 0 and count >= 0 and src + count <= storage_size and dest
