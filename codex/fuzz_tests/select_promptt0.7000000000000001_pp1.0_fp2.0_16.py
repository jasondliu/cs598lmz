import select
# Test select.select() by polling stdin and stdout

print('start')

while True:
    (rin, win, ein) = select.select([0,1], [], [])
    print('rin={0}'.format(rin))
    if 0 in rin:
        print('stdin is readable')
        stdinput = sys.stdin.readline()
        print('stdin = {0}'.format(stdinput))
    if 1 in rin:
        print('stdout is readable')
        stdouput = sys.stdout.readline()
        print('stdout = {0}'.format(stdoutput))
