import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)

# Test file:memdb1?mode=memory&cache=shared

# Test file:memdb1?mode=memory&cache=private

# Test file:memdb1?mode=memory

# Test file:memdb1?cache=shared

# Test file:memdb1?cache=private

# Test file:memdb1

# Test file::memory:?cache=shared

# Test file::memory:?cache=private

# Test file::memory:

# Test :memory:?cache=shared

# Test :memory:?cache=private

# Test :memory:

# Test unix-nonexistent-dir/foo.db

# Test unix-nonexistent-dir/foo.db?mode=memory&cache=shared

# Test unix-nonexistent-dir/foo.db?mode=memory&cache=private

# Test unix-nonexistent-dir/foo.db?mode=memory

# Test unix-none
