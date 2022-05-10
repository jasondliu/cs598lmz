import select
# Test select.select() function calls.
stdin = "/dev/stdin"
stderr = "/dev/stderr"
stdout = "/dev/stdout"
calls = [
    # Test input.
    ([stdin], [], []),
    ([stdin], [stderr], []),
    ([stdin], [], [stdout]),
    ([stdin], [stderr], [stdout]),
    ]
for x in calls:
    r, w, x = select.select(*x)
    # Check fd types.
    for f in r:
        assert(isinstance(f, file))
    for f in w:
        assert(isinstance(f, file))
    for f in x:
        assert(isinstance(f, file))
