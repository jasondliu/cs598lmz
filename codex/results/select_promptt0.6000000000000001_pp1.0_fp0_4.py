import select
# Test select.select()

# List of socket descriptors we want to wait for reading:
inputs = [ ]

# List of socket descriptors we want to wait for writing:
outputs = [ ]

# List of socket descriptors we want to wait for _exceptional_ conditions:
exceptional = [ ]

while inputs:
  print '\nwaiting for the next event'
  readable, writable, exceptional = select.select(inputs, outputs, inputs)

  # Handle inputs
  for s in readable:
    if s is server:
      # A "readable" server socket is ready to accept a connection
      connection, client_address = s.accept()
      print 'new connection from', client_address
      connection.setblocking(0)
      inputs.append(connection)
    else:
      data = s.recv(1024)
      if data:
        # A readable client socket has data
        print 'received "%s" from %s' % (data, s.getpeername())
        s.send(data)
        # Suppose we only have one client socket, and it's s.
