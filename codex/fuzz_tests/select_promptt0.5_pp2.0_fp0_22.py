import select
# Test select.select()
# Note that this test can't be run from IDLE.

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print(end - start)
