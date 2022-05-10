import select
# Test select.select

def test_select():
    import sys
    import time

    if not hasattr(select, 'select'):
        return

    # XXX Should test more fd's than this!!!
    r, w, x = select.select([sys.stdin], [], [], 10)
    if r:
        print('stdin ready for reading')
    else:
        print('stdin not ready for reading')

    # XXX Should test more fd's than this!!!
    r, w, x = select.select([], [sys.stdout], [], 10)
    if w:
        print('stdout ready for writing')
    else:
        print('stdout not ready for writing')

    # test exceptions
    try:
        select.select([], [], [], 'four')
    except TypeError:
        pass
    else:
        print('failed to raise TypeError for "select(..., timeout=\'four\')"')

    try:
        select.select([], [], [], object())
    except TypeError:
        pass
    else:
        print
