import codecs
codecs.lookup('utf-8')

import pandas as pd
import numpy as np



#df = pd.read_csv(r"C:\Users\Ganesh Patro\Dropbox\Exam_Papers\Converted_data\Analytics_Vidhya_Loan_Prediction.csv")
#df_new = pd.read_csv(r'C:\Users\Ganesh Patro\Documents\Ganesh_Backup\Analytics_Vidhya\Loan_Prediction_Dataset\test.csv')
df_new = pd.read_csv(r"test.csv")
df_new.head()

df_new['Total_Income'] = df_new['ApplicantIncome'] + df_new['CoapplicantIncome']
df_new['Loan_Status'] = "Y"
df = pd.read_csv(r"train.csv")
df.head()

df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome']
replace_map
