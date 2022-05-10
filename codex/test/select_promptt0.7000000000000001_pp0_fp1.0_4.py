import select
# Test select.select
#
# The output should look like:
#
# $ python3 select_echo_server.py
# starting up on localhost port 10000
# waiting for the next event
# new connection from ('127.0.0.1', 53728)
# waiting for the next event
# got message from ('127.0.0.1', 53728):
# 'This is the message.  It will be repeated.'
# waiting for the next event
# got message from ('127.0.0.1', 53728):
# 'This is the message.  It will be repeated.'
# waiting for the next event
# got message from ('127.0.0.1', 53728):
# 'This is the message.  It will be repeated.'
# waiting for the next event
# got message from ('127.0.0.1', 53728):
# 'This is the message.  It will be repeated.'
# waiting for the next event
# got message from ('127.0.0.1', 53728):
# 'This is the message.  It will be repeated.'
#
