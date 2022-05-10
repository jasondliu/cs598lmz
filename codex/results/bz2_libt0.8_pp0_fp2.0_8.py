import bz2
bz2.compress(pickle.dumps(mdp),9)

prb.write(mdp.name + '.mdp')
