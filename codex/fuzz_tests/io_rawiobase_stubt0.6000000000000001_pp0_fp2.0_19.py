import io
class File(io.RawIOBase):
   def fileno(self):
      return 42

with open('foo', 'wr') as f:
   f.write('This is foo!')

with open('bar', 'wr') as f:
   f.write('This is bar!')

with open('baz', 'wr') as f:
   f.write('This is baz!')

with open('qux', 'wr') as f:
   f.write('This is qux!')

with open('quux', 'wr') as f:
   f.write('This is quux!')

with open('corge', 'wr') as f:
   f.write('This is corge!')

with open('grault', 'wr') as f:
   f.write('This is grault!')

with open('garply', 'wr') as f:
   f.write('This is garply!')

with open('waldo', 'wr') as f:
   f.write('This is waldo!')

with open('fred', 'wr') as f:

