from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

while True:
  try:
    print(len(s.pack(int(input()))))
  except EOFError:
    break
