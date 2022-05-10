import types
types.ClassType = type

src = None
dst = None

def pythonError(msg):
	print msg

if len(CommandLine().args) > 2:
	src = CommandLine().args[2]
	if len(CommandLine().args) > 3:
		dst = CommandLine().args[3]
	else:
		base = os.path.basename(src)
		if base.endswith(".src"):
			baseTrimmed = base[:-4]
		if baseTrimmed.endswith(".py"):
			baseTrimmed = baseTrimmed + "c"
		temp = tempfile.mkstemp(prefix=baseTrimmed,suffix=".pyc")
		os.close(temp[0])
		dst = temp[1]
else:
	pythonError("Not enough parameters")
	exit(1)

f = open(src)
s = f.read()
f.close()

compiled = compile(s, src, "exec")
