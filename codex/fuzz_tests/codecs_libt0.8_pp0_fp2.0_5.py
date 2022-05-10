import codecs
codecs.open('treviews.csv', 'r', 'utf-8')

import pandas as pd
import re

df = pd.read_csv('treviews.csv', index_col=0)
df.head()

df.drop(['date','useful','funny','cool','text','review_id','stars'], axis=1, inplace=True)
df.head()

df2 = df[df.business_id.duplicated(keep=False)]
df2.head()

df3 = df2[df2.stars_y.duplicated(keep=False)]
df3.head()

df4 = df3[df3.user_id.duplicated(keep=False)]
df4.head()

df5 = df4.sort_values(['business_id','stars_y','user_id'], ascending=[True, True, False])
df5.head()

df6 = df5.groupby(['business_id','stars_y'], as_index=False).count()
df6.head
