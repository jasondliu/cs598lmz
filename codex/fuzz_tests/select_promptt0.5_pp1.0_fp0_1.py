import select
# Test select.select()

# Example 1
print(select.select([sys.stdin], [], [], 5))

# Example 2
timeout = 3
print(select.select([sys.stdin], [], [], timeout))
