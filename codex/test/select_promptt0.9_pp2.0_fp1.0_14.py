import select
# Test select.select() and select.error()
import select
select.select([], [], [], 0)
try:
    select.select([], [], [], -1)
except select.error as e:
    print("Got", e)

select.epoll([], 0)
