import select
# Test select.select() with a bad file descriptor.
# This used to raise a TypeError, but now it raises an OSError.
import time

class BadFile:
    def fileno(self):
        return 'abc'

for badfd in (BadFile(), 'abc'):
    try:
        select.select([], [], [], 0)
    except OSError as err:
        print(err)
    try:
        select.select([badfd], [], [], 0)
    except OSError as err:
        print(err)
    try:
        select.select([], [badfd], [], 0)
    except OSError as err:
        print(err)
    try:
        select.select([], [], [badfd], 0)
    except OSError as err:
        print(err)
    try:
        select.select([badfd], [badfd], [badfd], 0)
    except OSError as err:
        print(err)

# Test select.select() with an invalid timeout value.
