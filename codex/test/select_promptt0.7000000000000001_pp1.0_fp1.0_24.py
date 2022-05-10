import select
# Test select.select()
# Set up some pipes and an input stream
pr, pw = os.pipe()
for f in (pr, pw):
    print >> sys.stderr, 'fds=', f
    fcntl.fcntl(f, fcntl.F_SETFL, os.O_NONBLOCK)    
input = [pr]
# Run a select to wait for input on the pipes
print >> sys.stderr, 'about to select'
inputready, outputready, exceptready = select.select(input,[],[])
print >> sys.stderr, 'inputready =', inputready
# Loop and copy the pipe contents to stdout
for fd in inputready:
    if fd == pr:
        data = os.read(pr, 1024)
