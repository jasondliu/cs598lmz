import _struct
# Test _struct.Struct.format_size.
# This is tested through the unpack method.
# See also issue #18293.
print(_struct.Struct("=6i").format_size("<6i"))
print(_struct.Struct("=6i").format_size("=6i", "<6i"))
print(_struct.Struct("=6i").format_size("=3q"))
print(_struct.Struct("=6i").format_size("=3q", "<3q"))
import fractions
# Test fractions.gcd().
print(fractions.gcd(5, 2))
print(fractions.gcd(7, 31))
print(fractions.gcd(12, care_less=13))
import _socket
# Test _socket.getaddrinfo().
print(_socket.getaddrinfo("localhost", 80))
print(_socket.getaddrinfo("localhost", 80, 0, 0, socket.SOL_TCP))
print(_socket.getaddrinfo("localhost", 80, 0, 0, socket.SOL_TCP, socket.IPPROTO_IP))
print(_socket.getaddrinfo
