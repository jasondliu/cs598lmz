import select
# Test select.select
print select.select([], [], [], 0.5)
print select.select([], [], [], 0.5)
print select.select([], [], [], 0.5)
print select.select([], [], [], 0.5)

# Test select.error
try:
    select.select([], [], [], 0.5)
except OSError:
    print "OSError"
except select.error:
    print "select.error"
