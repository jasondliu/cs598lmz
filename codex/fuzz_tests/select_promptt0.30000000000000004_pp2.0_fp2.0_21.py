import select
# Test select.select()

# Select on stdin
r, w, e = select.select([sys.stdin], [], [], 0)
if r:
    print "stdin ready"
else:
    print "stdin not ready"

# Select on stdout
r, w, e = select.select([], [sys.stdout], [], 0)
if w:
    print "stdout ready"
else:
    print "stdout not ready"

# Select on stderr
r, w, e = select.select([], [], [sys.stderr], 0)
if e:
    print "stderr ready"
else:
    print "stderr not ready"
</code>
Output:
<code>stdin ready
stdout ready
stderr ready
</code>

