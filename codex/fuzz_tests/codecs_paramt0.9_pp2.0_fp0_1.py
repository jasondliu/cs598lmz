import codecs
codecs.register_error('replace_with_space', lambda e: (u' ','ignore'))
df.to_csv('final_table/1611/clean_hotels1611_new.csv',encoding='utf-8',index=False)
df.to_csv('final_table/1611/clean_hotels1611_new.csv',encoding='utf-8',index=False)
 
 

"""
Convert the file type to be read by R
"""
 
import pandas as pd
df=pd.read_csv('final_table/1611/clean_hotels1611.csv',encoding='utf-8')
df=df.drop(df.columns[0],axis=1)
df.to_json('final_table/1611/clean_hotels1611.json',orient='records',force_ascii=False)

df.to_json('final_table/1611/clean_hotels1611.json',orient='records',force_ascii=False)
import pandas as pd
df=pd.read_
