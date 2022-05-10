import socket
# Test socket.if_indextoname.

def check(family, expected_name):
    # Get the ifname of the loopback interface.
    ifname = socket.if_indextoname(1)
    if ifname != expected_name:
        print("loopback ifname:", `ifname`)
        raise TestFailed("bad loopback ifname")

check(socket.AF_INET, "lo0")

check(socket.AF_INET6, "lo0")
