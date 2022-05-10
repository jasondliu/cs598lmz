import bz2
bz2.compress('a'*100000)

import cProfile, pstats, StringIO
pr = cProfile.Profile()
pr.enable()

# ... do something ...

pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()
