import sys, threading
threading.Thread(target=lambda:sys.stdout.write("\n"*999)).start()
import datetime
from datetime import datetime
from datetime import timedelta
import time
import random


warnings.filterwarnings('ignore')

#loading in the weather data as 2D array
weather2D_array=[]
with open("/Users/Harry/Desktop/weather_data.csv") as f:
    reader=csv.reader(f)
    for row in reader:
        weather2D_array.append(row)

#Turning weather array into a DF
weather_df=pd.DataFrame(weather2D_array)

#the first row contains the headers of the DF, so we delete it
weather_df=weather_df.iloc[1:,:]

#Changing headers
weather_df.columns=['Date','Max_temp','Dew_point','Visibilty','Wind_speed','Precipitation_mm','Events']

#Taking out the day of the week
weather_df['Date']=pd.to_datetime(weather_df['Date'])
weather_df
