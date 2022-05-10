fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "test"
fn.__dict__ = {}

s = pickle.dumps(fn)
dump_filename = 'test.dump'
with open(dump_filename, 'wb') as f:
    f.write(s)
print("Dump written to %s" % dump_filename)
