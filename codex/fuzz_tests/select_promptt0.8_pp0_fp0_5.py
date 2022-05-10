import select
# Test select.select():
# select.select([], [], [], 0)

try:
    select.select([], [], [], -1)
except ValueError:
    print("ValueError")

# Test select.poll():
# select.poll()
try:
    select.poll()
except:
    print("Error")

# Test select.epoll():
# select.epoll()
try:
    select.epoll()
except:
    print("Error")

# Test select.kepoll():
# select.kepoll()
try:
    select.kepoll()
except:
    print("Error")

# Test select.devpoll():
# select.devpoll()
# select.devpoll(-1)
try:
    select.devpoll()
except:
    print("Error")
try:
    select.devpoll(-1)
except ValueError:
    print("ValueError")

# Test select.modify1():
s = select.select([], [], [])
# select.modify1(s, -1)
try:
    select
