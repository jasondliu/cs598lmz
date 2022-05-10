import select
# Test select.select error handler
def f():
  # set bad file descriptors
  rd, wr = -1, -1
  try:
    select.select([rd], [wr], [])
  except ValueError:
    pass
  else:
    print 'GOT IT and no ValueError'


f()
