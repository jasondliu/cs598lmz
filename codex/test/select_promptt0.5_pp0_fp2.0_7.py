import select
# Test select.select()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',0))
s.listen(1)

(c,a) = s.accept()

