fn = lambda: None
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0

# Test sys.flags
import sys
sys.flags = sys.flags
sys.flags.debug = False
sys.flags.optimize = 0
sys.flags.dont_write_bytecode = False
sys.flags.no_site = False
sys.flags.ignore_environment = False
sys.flags.verbose = False
sys.flags.bytes_warning = False
sys.flags.quiet = False
sys.flags.hash_randomization = False
sys.flags.isolated = False
sys.flags.utf8_mode = False
sys.flags.dev_mode = False

# Test sys.warnoptions
sys.warnoptions = ['ignore::DeprecationWarning']

# Test sys.argv
sys.argv = [sys.argv[0]]
sys.argv = [sys.argv[0], "--help"]

# Test sys.path
sys.path = sys.path
sys.path.append('/foo')
sys.path.append('/foo')
sys.path.
