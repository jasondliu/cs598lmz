import codecs
codecs.register_error('strict', codecs.ignore_errors)

# wrap _readline() to ignore \r.
def readline(self):
    return self._readline().replace('\r', '')

# replace Readline.readline
Readline.readline = readline

# start a line-reader loop
rl = Readline()
while 1:
    line = rl.readline()
    if not line:
        break
    print repr(line)
