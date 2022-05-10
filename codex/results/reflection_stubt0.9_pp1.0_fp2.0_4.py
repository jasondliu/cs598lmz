fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__globals__['__builtins__'] = dict()
fn.__globals__['__builtins__']['object'] = object
code = fn.__code__
return marshal.dumps(code)
'''

vuln = (1, 'c', 'sys.exit()', ())

a = marshal.dumps(vuln)

print '[*] Length of vulnerability code:', len(a)

#print a

try:
    marshal.loads(a)
except SystemExit:
    print '[!] Payload triggered'
