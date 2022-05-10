import select
# Test select.select()
socket_read = []
socket_write = []
socket_error = []
timeout = 0
socket = select.select(socket_read, socket_write, socket_error, timeout)
