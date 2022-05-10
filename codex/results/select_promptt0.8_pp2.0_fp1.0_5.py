import select
# Test select.select on sockets with no I/O

# Try to create a socket in each possible state, and call select() on it
# to see if it reports any readiness.

def test_socket_states(family, type, proto=0):
    states = [socket.socket,
              lambda family_, type_, proto_: socket.socket(family_, type_, proto_).close(),
              lambda family_, type_, proto_: socket.socket(family_, type_, proto_).bind(("0.0.0.0", 0)),
              lambda family_, type_, proto_: socket.socket(family_, type_, proto_).bind(("0.0.0.0", 0)).close(),
              lambda family_, type_, proto_: socket.socket(family_, type_, proto_).bind(("0.0.0.0", 0)).listen(),
              lambda family_, type_, proto_: socket.socket(family_, type_, proto_).bind(("0.0.0.0", 0)).listen().close(),
              lambda family
