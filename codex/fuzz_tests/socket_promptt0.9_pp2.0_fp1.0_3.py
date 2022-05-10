import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
# Test multiply parentheses
print((((3)))+ 2)
# Test getattr with gt
print(getattr(sys, "gt".strip("t")))
# Test not is
print(not isinstance(5, int))
# Test not in
print(5 not in [1,2,3])
# Test continue
for i in range(10):
    if i == 5:
        continue
# Test break
for i in range(10):
    if i == 5:
        break
# Test list and for with else
for i in [] :
    if i == 5:
        break
else:
    print("Never executed because after for")
# Test division float with float
print(1.0 / 3.0)
# Test division float with int
print(1.0 / 3)
print(1 / 3.0)
# Test division int with int
print(1 // 3)
# Test division modulo with float
print(1.0 % 3)
print(1 % 3.0)
# Test division int
