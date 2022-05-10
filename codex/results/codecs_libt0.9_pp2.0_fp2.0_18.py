import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
#print('hello world')
import pandas
fp=pandas.read_csv(r'D:\Dropbox\utilities\sample.csv')
print(fp)
</code>
all_df = all_df.transpose
print(all_df)
if i run the above code then i am getting the error like
UnicodeEncodeError: 'charmap' codec can't encode characters in position 1786-1787: character maps to 
please suggest me on this.
Thanks in advance,
Gaju.


A:

Use BOM_UTF8:
<code>all_df.to_csv(filename, encoding='utf_8_sig')
</code>

