import codecs
codecs.register_error('strict', codecs.ignore_errors)
sys.stdin = codecs.getreader('utf8')(sys.stdin.detach())
sys.stdout = codecs.getwriter('utf8')(sys.stdout.detach())
sys.stderr = codecs.getwriter('utf8')(sys.stderr.detach())

# get all the lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# parse input
N, M, K = map(int, lines[0].split())
rows = [list(map(int, line.split())) for line in lines[1:N+1]]
cols = [list(map(int, line.split())) for line in lines[N+1:N+M+1]]

# solve problem
solution = 0

# output result
print(solution)
