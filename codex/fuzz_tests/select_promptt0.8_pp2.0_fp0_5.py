import select
# Test select.select() input_list, timeout
# Should return immediately
print(select.select([sys.stdin], [], [], 0.0))
print(select.select([sys.stdin], [], [], 0.0)[0])
# Should return immediately
print(select.select([sys.stdin], [], [], 0.0)[0][0])

# Test select.select() input_list, timeout
# Should return immediately
print(select.select([sys.stdin], [], [], 0.0)[0][0].fileno())
