import select
# Test select.select blocks with a zero timeout
import socket, time
r, w, x = select.select([], [], [], 0.0)
