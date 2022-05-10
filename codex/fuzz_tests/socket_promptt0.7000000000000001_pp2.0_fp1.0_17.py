import socket
# Test socket.if_indextoname() with invalid index.
import socket
try:
    socket.if_indextoname(2**32-1)
except OverflowError as e:
    print(e)

try:
    socket.if_indextoname(-1)
except OverflowError as e:
    print(e)

try:
    socket.if_indextoname(2**32)
except OverflowError as e:
    print(e)

try:
    socket.if_indextoname(-2)
except OverflowError as e:
    print(e)

try:
    socket.if_indextoname(0)
except OSError as e:
    print(e)
