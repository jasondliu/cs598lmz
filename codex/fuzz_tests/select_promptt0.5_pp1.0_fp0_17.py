import select
# Test select.select()

# Create a couple of sockets
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Give them a little time to connect to each other
time.sleep(1)

# See if they are ready to read or write
print(select.select([s1], [s2], [], 0))

# Close them and see if they are still ready to read or write
s1.close()
s2.close()
print(select.select([s1], [s2], [], 0))
