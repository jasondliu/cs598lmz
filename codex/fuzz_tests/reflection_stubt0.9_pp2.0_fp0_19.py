fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

bailout(args)
p.expect_exact('Done.')
p.close()
