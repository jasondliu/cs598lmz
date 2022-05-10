import mmap
# Test mmap.mmap()
mm = mmap.mmap(-1, 100)

while True:
  ans = input('>')
  if ans == 'done':
    break
  mm.seek(0)
  mm.write(ans.encode())
  mm.seek(0)
  print(mm.read(100).decode())

mm.close()
