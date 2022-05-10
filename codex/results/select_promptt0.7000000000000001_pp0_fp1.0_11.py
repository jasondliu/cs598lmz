import select
# Test select.select
# select.select([input_sockets], [output_sockets], [exception_sockets])

input_sockets, output_sockets, exception_sockets = select.select(
    [sys.stdin], [], [], 1.0)
