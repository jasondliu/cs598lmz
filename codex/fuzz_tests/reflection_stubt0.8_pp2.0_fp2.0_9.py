fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi()
a = sys.modules['__main__']
import os
with open('file', 'w') as f:
	f.write('import sys')
	f.write('\n')
	f.write(f'code_object = compile("{fn.__code__}", "foo", "exec")')
	f.write('\n')
	f.write('exec(code_object)')
p = os.popen('python file')
sys.exit(0)
