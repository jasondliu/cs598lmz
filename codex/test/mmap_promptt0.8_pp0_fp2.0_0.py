import mmap
# Test mmap.mmap before it gets imported by our modules.
# Some systems will raise ENODEV if they don't have any devices to
# mmap.  Other systems will raise EINVAL.
# It is better to test it in the setup step, so that the user is shown
# the right errors and knows the cause.
try:
    with mmap.mmap(-1, 1024):
        pass
except (OSError, IOError):
    raise SystemExit('Your system does not support mmap.mmap(-1, 1024).\n'
                     'This is required by Twisted.')


with open(join(dirname(__file__), '_version.py')) as v:
    exec(v.read())


class package_unavailable(Exception):
    """A required package is not available."""


def runSetup(config):
    """
    Run the setup process.

    @param config: Configuration to run with.
    @type config: L{twisted.python.dist.Distribution}
    """
    config.runWithEggs()


config = Distribution()
