import select
# Test select.select()

import select, socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 25000))
s.listen(5)
