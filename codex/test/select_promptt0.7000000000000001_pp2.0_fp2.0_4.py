import select
# Test select.select
def select_test():
    # The select() function takes three lists of sockets and waits until one or more of the sockets is ready for some kind of I/O.
    # The first list, read_list, contains the sockets we're interested in reading from.
    # The second list, write_list, contains the sockets we're interested in writing to.
    # The third list, except_list, contains the sockets we're interested in getting exceptional condition notifications for.
    # The function returns three lists containing only the sockets that are ready for the requested operation.
    read_list, write_list, except_list = select.select(read_list, write_list, except_list, timeout)
    # The timeout argument is optional and specifies a time-out as a floating point number in seconds.
    # When the time-out argument is omitted the function blocks until at least one socket is ready.
    # A time-out value of zero specifies a poll and never blocks.
    # A negative time-out specifies an infinite time-out.
    # The following example shows how to use the select() function to multiplex the reading of the standard input and
