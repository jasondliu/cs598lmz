import select
# Test select.select()
#
# input_list = [sys.stdin, ]
# timeout = 5
# readable, writable, exceptional = select.select(input_list, [], [], timeout)
# if readable:
#     input_data = sys.stdin.readline().strip()
#     print "you entered: %s" % input_data
# else:
#     print "no input. timeout %d seconds." % timeout

# input_list = [sys.stdin, ]
# timeout = 5
# readable, writable, exceptional = select.select(input_list, [], [], timeout)
# for s in readable:
#     input_data = sys.stdin.readline().strip()
#     print "you entered: %s" % input_data
# else:
#     print "no input. timeout %d seconds." % timeout

# input_list = [sys.stdin, ]
# timeout = 5
# while True:
#     readable, writable, exceptional = select.select(input_list, [], [], timeout)
#     if not (readable
