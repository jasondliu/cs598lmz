import bz2
bz2file = bz2.BZ2File('../Data/EpicOptionsChain_FB.csv.bz2') 
large_csv = pd.read_csv(bz2file, encoding = "ISO-8859-1", error_bad_lines = False, warn_bad_lines = False)
large_csv.head(5)

# LOAD SUMMER OF 2016 KAGGLE ACQUIRED HISTORICAL OPTION DATA FROM FACEBOOK
#bz7_file = sc.textFile('../Data/df_FB_Sep.csv.bz2')
#bz2file = bz2.BZ2File('../Data/df_FB_Sep.csv.bz2') 
#df_FB_Sep = pd.read_csv(bz2file, encoding = "ISO-8859-1", error_bad_lines = False, warn_bad_lines = False)
#df_FB_Sep.head(5)

# LOAD SUMMER OF 2016 KAGGLE ACQUIRED HISTORICAL OPTION DATA FROM APPLE
#bz7
