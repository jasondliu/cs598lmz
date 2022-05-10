fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
sys.getrefcount(gi)
 
# options to invoke
# PYTHONMALLOC=debug python3 ./malloc_offset.py 
# PYTHONMALLOC=debug gdb --args python3 ./malloc_offset.py 
# valgrind --tool=memcheck --leak-check=full --show-leak-kinds=all --track-origins=yes python3 ./malloc_offset.py
