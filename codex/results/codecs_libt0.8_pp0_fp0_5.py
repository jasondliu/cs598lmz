import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#==================================================================
#============Set the working directory============================
#==================================================================
os.chdir(r"C:\Users\janko.a\Desktop\Udemy_Courses\DataScience\Kaggle\Competitions")


os.getcwd()

#==================================================================
#============Importing Data=======================================
#==================================================================
df = pd.read_csv("train.csv")
df.head(3)
df.shape
df.describe()

de = pd.read_csv("test.csv")
de.head(3)
de.shape

df.describe()


#==================================================================
#============Data Exploration and Visualization====================
#==================================================================

#==========================
#==Univariate Analysis====
#==========================

#Histogram of Target variable
df_temp = pd.DataFrame(columns=['target'])
df_temp['target'] = df.target
sns.distplot(df
