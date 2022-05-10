import select
# Test select.select is accessible
x = select.select
s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 6666))
