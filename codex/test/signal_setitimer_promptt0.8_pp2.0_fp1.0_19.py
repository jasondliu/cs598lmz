import signal
# Test signal.setitimer
signal.setitimer(0, 1, 0)
''' % (srcdir, len(tests_srcdir + tests_not_srcdir)))
# ------------------------------------------------------------
# Isolated tests
# ------------------------------------------------------------

quiet = True

unpack_test(open('test-unpack', 'w'), quiet)

if quiet:
  sys.stdout.write('1..%d\n' % len(tests_srcdir + tests_not_srcdir))

# ------------------------------------------------------------
# Settings
# ------------------------------------------------------------

# The binaryen interpreter (JavaScript version)
binterp = None

binterp_command = [os.path.join(binaryen_bin, 'binaryen-shell.js')]

reftest_prefix = os.path.join(binaryen_bin, 'asm2wasm')

'''
use_reftest = False # slow, and not all tests pass this way

