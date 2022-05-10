import select
# Test select.select

def get_readable_sockets(sockets):
    """
    Returns a list of sockets that have data to be read.

    """
    readable_sockets = []
    while True:
        try:
            readable_sockets, _, _ = select.select(sockets, [], [], 0)
        except select.error:
            continue
        else:
            break
    return readable_sockets

def get_writable_sockets(sockets):
    """
    Returns a list of sockets that are ready to be written to.

    """
    writable_sockets = []
    while True:
        try:
            _, writable_sockets, _ = select.select([], sockets, [], 0)
        except select.error:
            continue
        else:
            break
    return writable_sockets

def get_exceptional_sockets(sockets):
    """
    Returns a list of sockets that have raised exceptions.

    """
    exceptional_sockets = []
