import bz2
bz2_data = bz2.BZ2File('data/train.ft.txt.bz2')
data = [x.decode('utf-8') for x in bz2_data.readlines()]
data[:2]

__label__1 Great CD: My lovely Pat has one of the GREAT voices of her generation. I have listened to this CD for YEARS and I still LOVE IT. When I\'m in a good mood it makes me feel better. A bad mood just evaporates like sugar in the rain. This CD just oozes LIFE. It is a truly LIFE-AFFIRMING CD. Patricia is an amazing composer and I hope she continues to do what she does best for a long time to come.

__label__2 One of the last great bookstores: This is one of the last great bookstores. If you are in Rome, do not miss it. I found everything I was looking for in English, Italian and French, and I even found a few things I didn\'t even know I was looking for. The staff was very helpful and the prices were excellent.

len(data)

3600000

import random

