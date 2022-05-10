import select
# Test select.select, then call it to wait for input on stdin.
# We expect that stdin, stdout, stderr are all readable and writable.
# stdin == 0, stdout == 1, stderr == 2, on all platforms.
# We expect that select.select will never return lists containing
# stdin if stdin is connected to a tty, because a tty is a character
# device, and character devices are always readable.

print(select.select.__doc__)

if sys.platform.startswith('win'):
    # A bug in the Windows select() implementation means you can't
    # distinguish between an empty list and an error.
    # So skip this test on Windows.
    print("Skipping test on windows")
    sys.exit(0)

try:
    r, w, x = select.select([], [], [], 0)
except ValueError as msg:
    print("Got expected exception:", msg)
else:
    print("Expected exception, got", r, w, x)

r, w, x = select.select([sys
