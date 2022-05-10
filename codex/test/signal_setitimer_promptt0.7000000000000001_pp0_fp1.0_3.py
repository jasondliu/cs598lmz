import signal
# Test signal.setitimer()
#
# This test is not included in the main test suite because it requires
# root priviledges.
#
# If the test is run using 'sudo', then this program will attempt to
# raise a real-time signal every second. If the test is run as a
# non-privileged user, this program will only attempt to raise a
# virtual timer signal.
#
# The test program is supposed to exit when the test is complete. If
# it fails to do so, it will be killed after 5 minutes.
#
# A. S. Hodel <scotte@ieee.org>
#

