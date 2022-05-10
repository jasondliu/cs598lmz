import socket
# Test socket.if_indextoname()
#
# This test is intended to be run by the automated test harness.  It is
# not intended to be run manually.
#
# This test assumes that the test harness has already set up the network
# interface.
#
# This test requires that the test harness has set up the following
# environment variables:
#
#     TEST_IF_NAME
#
# This test uses the following environment variables:
#
#     TEST_IF_NAME
#
# This test uses the following configuration file variables:
#
#     TEST_IF_NAME
#
# This test uses the following functions:
#
#     test_begin
#     test_check
#     test_end
#
# This test prints PASS or FAIL.

test_begin "socket-if_indextoname"

if [ "$TEST_IF_NAME" = "" ]; then
    test_check 1 false
    test_end 1
fi

test_check 0 test "$(socket.if_indextoname "$TEST_IF_NAME")" = "$TEST_IF_NAME"
test_check
