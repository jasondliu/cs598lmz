import select
# Test select.select() using stdin, stdout, and stderr
print(select.select([sys.stdin], [], [], 1))    # Selects stdin only if data is ready
print(select.select([sys.stdin], [], [], 0))    # Selects stdin only if data is ready
print(select.select([sys.stdin], [], [], 60))   # Selects stdin only if data is ready

print(select.select([], [sys.stdout], [], 1))   # Selects stdout only if data can be sent
print(select.select([], [sys.stdout], [], 0))   # Selects stdout only if data can be sent
print(select.select([], [sys.stdout], [], 60))  # Selects stdout only if data can be sent

