import select
# Test select.select()
reader, writer, excpt = select.select( [r], [], [], 0 )
assert_equal( len(reader), 0 )

reader, writer, excpt = select.select( [r, s2], [], [], 0 )
assert_equal( len(reader), 1 )

reader, writer, excpt = select.select( [r, s2], [], [], 1 )
assert_equal( len(reader), 1 )

reader, writer, excpt = select.select( [r, s2], [], [], 2 )
assert_equal( len(reader), 0 )

assert_equal( os.read(r.fileno(), 1024), "abc" )
assert_equal( os.read(r.fileno(), 1024), "def" )
