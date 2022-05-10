import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor

# start = time.time()
# with ThreadPoolExecutor(max_workers=5) as exe:
#     for i in range(5):
#         exe.submit(slow_systemcall)
# end = time.time()
# print('Took %.3f seconds' % (end - start))

# Test ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor

start = time.time()
with ProcessPoolExecutor(max_workers=5) as exe:
    for i in range(5):
        exe.submit(slow_systemcall)
end = time.time()
print('Took %.3f seconds' % (end -
