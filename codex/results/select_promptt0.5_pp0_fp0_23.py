import select
# Test select.select()

# Create some pipes
r, w = os.pipe()
r2, w2 = os.pipe()

pid = os.fork()
if pid:
    os.close(r)
    os.close(r2)
    # Close child ends in parent
    print('Parent doing some work')
    # Do some 'work'
    time.sleep(3)
    print('Parent sending message')
    # Send message to child
    os.write(w, b'Your turn')
    # Wait for child
    print('Parent waiting for second message')
    os.read(r2, 1000)
    print('Parent got second message')
    # Clean up
    os.close(w)
    os.close(w2)
else:
    os.close(w)
    os.close(w2)
    # Close parent ends in child
    print('Child waiting for message')
    # Wait for message from parent
    m = os.read(r, 1000)
    print('Child got message:', m)
    # Send reply to parent
    print('Child
