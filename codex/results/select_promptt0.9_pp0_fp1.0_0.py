import select
# Test select.select()
print('before select():', time.time())
readable, writeable, exceptional = select.select([sys.stdin], [], [], 20)
print('after select():', time.time())
print('readable:', readable)
print('writeable:', writeable)
print('exceptional:', exceptional)
