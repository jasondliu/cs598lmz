import io
# Test io.RawIOBase
import shelve
import gdb, gdb.xinterface

print('Testing print_gdb_style for a string.')
value = "my string"
stringio = io.StringIO()
# Test that rawio hides the rawio methods from dir().
assert 'isatty' not in dir(stringio)
assert 'fileno' not in dir(stringio)
assert 'read' not in dir(stringio)
assert not hasattr(stringio, 'isatty')
assert not hasattr(stringio, 'fileno')
assert not hasattr(stringio, 'read')

gdb.print_gdb_style(value, stringio)
assert stringio.getvalue() == '"my string"\n'

gdb.print_gdb_style(value, stringio)
assert stringio.getvalue() == '"my string"\n"my string"\n'

print('Testing print_gdb_style for a tuple.')
value = ('one', 2, 'three')
stringio = io.StringIO()
gdb.print_g
