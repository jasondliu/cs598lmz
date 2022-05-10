import socket
# Test socket.if_indextoname on a bogus interface index.
print(socket.if_indextoname(-1))
EOF
if [ $? -eq 0 ]; then
  fail "we shouldn't be able to convert -1 to an interface"
fi

$python <<EOF
import socket
# Test socket.if_indextoname on a bogus interface index.
print(socket.if_indextoname(0xffffffff))
EOF
if [ $? -eq 0 ]; then
  fail "we shouldn't be able to convert 4294967295 to an interface"
fi

$python <<EOF
import socket
# Test socket.if_indextoname on a valid interface index.
print(socket.if_indextoname(1))
EOF
if [ $? -ne 0 ]; then
  fail "we should be able to convert 1 to an interface"
fi

$python <<EOF
import socket
# Test socket.if_indextoname on a valid interface index.
print(socket.if_indextoname(2))
EOF
if [ $? -ne 0 ]; then
