import socket
# Test socket.if_indextoname()

if __name__ == '__main__':
    import sys
    import os
    import unittest
    from test import support

    if not hasattr(socket, "if_indextoname"):
        raise support.TestSkipped("Platform has no socket.if_indextoname()")

    # get all (valid) interface indices
    indices = []
    max_possible_index = -1
    for name in os.listdir("/sys/class/net/"):
        try:
            with open("/sys/class/net/" + name + "/ifindex") as f:
                index = int(f.read())
        except EnvironmentError:
            continue
        if index > max_possible_index:
            max_possible_index = index
        indices.append(index)

    # generate a list of invalid indices
    invalid_indices = []
    i = 1
    while len(invalid_indices) < len(indices):
        if i not in indices:
            invalid_indices.append(i)
        i += 1
