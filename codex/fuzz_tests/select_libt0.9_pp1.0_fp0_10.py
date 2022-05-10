import selectors
import sys
import lab6_map
import libfoolang


print('main.py: Running...')

ctx = libfoolang.AnalysisContext()
u = ctx.get_from_buffer('main.txt', b'example')
if u.diagnostics:
    for d in u.diagnostics:
        print(d)
    sys.exit(1)

ctx.populate_lexical_envs([u])

u.root.p_display_fsets()

for f_set in u.root.p_find_fset(None):
    print("Found FSet for {}".format(f_set))
    for node in f_set.p_find_matching_nodes(None, None):
        print("  Matches {}".format(node))

print('main.py: Done.')
