import select
# Test select.select()
for i in range(10):
    readable, writable, exceptional = select.select(
                                         [sys.stdin],
                                         [],
                                         [],
                                         2)
    if not (readable or writable or exceptional):
        print("Time out!")
    else:
        print("\nCan do IO now!")
