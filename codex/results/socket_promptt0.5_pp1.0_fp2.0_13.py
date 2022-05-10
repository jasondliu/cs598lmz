import socket
# Test socket.if_indextoname()
import select
# Test select.select()
import errno

def get_if_index(if_name):
    # Get interface index
    try:
        if_index = socket.if_nametoindex(if_name)
    except OSError as err:
        if err.errno == errno.ENODEV:
            print("Network interface '{}' not found.".format(if_name))
            if_index = 0
        else:
            raise
    return if_index

def get_if_name(if_index):
    # Get interface name
    try:
        if_name = socket.if_indextoname(if_index)
    except OSError as err:
        if err.errno == errno.ENODEV:
            print("Network interface with index '{}' not found.".format(if_index))
            if_name = 0
        else:
            raise
    return if_name

def get_if_names():
    # Get all interface names
    if_names = []
   
