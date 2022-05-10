import socket
# Test socket.if_indextoname() across all interfaces
from time import time

from check import (
    MSG,
    WRONG_IF,
    check_value,
    error,
    msg_count,
    msg_count_all,
    save_failed
)
from check_interface import (
    test_interface,
    test_empty,
    test_duplicate,
    test_invalid,
    test_valid,
    print_config
)
from get_ifindex import (
    get_ifindex
)
from print_result import (
    print_result_count,
    print_result
)

# Get current interface list
ifindexes = get_ifindex()

# Check current interface list
count, count_all = test_interface(socket.if_indextoname,
                                  ifindexes,
                                  MSG, test_invalid, test_valid, test_empty,
                                  test_duplicate,
                                  WRONG_IF, error, save_failed)

