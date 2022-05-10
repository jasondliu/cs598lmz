import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# http://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python
Data=pd.read_csv(r"/Users/admin/Desktop/Data.csv")

# Data=pd.read_excel(r"/Users/admin/Desktop/Data.xlsx")
#------------------------------------------------------------------------------
# Cleaning


#https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-certain-columns-is-nan
Data['GDP per Capita']=Data['GDP per Capita'].apply(lambda x : np.nan if x=="No Data" else x)

# Data=Data.dropna()

#replace
Data['GDP per Capita']=Data['GDP per Capita'].replace({" No Data":np.nan})

