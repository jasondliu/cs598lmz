from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.BZ2File('../data/train.csv.bz2').read())

# import pandas as pd
# pd.read_csv('../data/train.csv')

# import pandas as pd
# import bz2
# with bz2.BZ2File('../data/train.csv.bz2') as f:
#     pd.read_csv(f)

# import pandas as pd
# import bz2
# with bz2.BZ2File('../data/train.csv.bz2') as f:
#     pd.read_csv(f, compression='bz2')

# import pandas as pd
# import bz2
# pd.read_csv('../data/train.csv.bz2', compression='bz2')

# import pandas as pd
# import bz2
# with bz2.BZ2File('../data/train.csv.bz2') as f:
#     pd.read_csv(
