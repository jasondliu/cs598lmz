import select
# Test select.select()?
print('sys.stdin', sys.stdin)
print('sys.stdout', sys.stdout)
print('sys.stderr', sys.stderr)
print('select.select(sys.stdin, (), ())', select.select([sys.stdin], [], []))

sys.stdout.flush()
sys.stderr.flush()


#---
# Error (but I can't reproduce it):
#---

#print('select.epoll()')
#epoll = select.epoll()
#print('select.poll()')
#poll = select.poll()
