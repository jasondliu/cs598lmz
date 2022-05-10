import select
# Test select.select() for reading on a descriptor
# with the event loop in the background

def read(fd):
    data = os.read(fd, 100)
  
