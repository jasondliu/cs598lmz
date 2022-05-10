import socket
# Test socket.if_indextoname()

print("Test if_indextoname()")

if_indextoname = socket.if_indextoname

print("if_indextoname(0) ->", if_indextoname(0))
print("if_indextoname(1) ->", if_indextoname(1))
print("if_indextoname(2) ->", if_indextoname(2))
print("if_indextoname(3) ->", if_indextoname(3))
print("if_indextoname(4) ->", if_indextoname(4))
try:
    print("if_indextoname(5) ->", if_indextoname(5))
except OSError as e:
    print("if_indextoname(5) ->", e)

print("if_indextoname(6) ->", if_indextoname(6))
print("if_indextoname(7) ->", if_indextoname(7))
print("if_indexton
