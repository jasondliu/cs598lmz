import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 10)
signal.setitimer(signal.ITIMER_PROF, 10)
signal.setitimer(signal.ITIMER_VIRTUAL, 10)

import json
# Test json.JSONDecodeError
try:
    json.loads("{")
except json.JSONDecodeError as e:
    print(e.msg)
    print(e.lineno)
    print(e.colno)
    print(e.doc)
    print(e.pos)
    print(e.end)

# Test json.JSONDecodeError with trailing comma
try:
    json.loads("{,}")
except json.JSONDecodeError as e:
    print(e.msg)
    print(e.lineno)
    print(e.colno)
    print(e.doc)
    print(e.pos)
    print(e.end)

import ctypes
# Test ctypes._Pointer
