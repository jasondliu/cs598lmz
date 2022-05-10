import bz2
bz2.__version__

with open('attack_raw.dat', 'rb') as f:
    data = f.read()
    attack_compressed = bz2.compress(data)
    print(len(data), len(attack_compressed))
    sys.exit()
    with open('attack2.dat', 'wb') as f2:
        f2.write(attack_compressed)
