import select
# Test select.select() for reading and writing simultaneously
# on stdin and stdout.

print "Enter some text"
print "and watch select report that it is both readable and writable."

while 1:
    (r, w, e) = select.select([sys.stdin], [sys.stdout], [], 10)
    if sys.stdin in r:
        line = sys.stdin.readline()
        if not line: break    # EOF, exit
        sys.stdout.write(line)
        sys.stdout.flush()
    if sys.stdout in w:
        print "writable"
    if e:
        print "exception"
"""

# ======================================================================
#                       --- select.epoll ---
# ======================================================================

# Backported from Python 2.6.
# poll() replacement using epoll(4) if available.
# Copyright (C) 2006  Jeroen Ruigrok van der Werven <asmodai@in-nomine.org>
#
# This library is free software; you can redistribute it and/or
#
