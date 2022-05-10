import signal
# Test signal.setitimer()
#
# This test needs to be run in a separate process, as it uses
# setitimer() which will not work in the same process as the test
# driver.

# This test also needs to be run as root, as it uses RLIMIT_CPU...
if os.geteuid() != 0:
    raise RuntimeError("you need to be root")

