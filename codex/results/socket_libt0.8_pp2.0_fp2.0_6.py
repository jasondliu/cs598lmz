import socket
import time  # Add this import
import sqlite3
import datetime

# Change this to your own username! 
username = "ZhangJ"

# Get the hostname
host = socket.gethostname()

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = status._json
        my_id = decoded['user']['screen_name']
        #print(my_id)
        #get tweets
        if my_id == username:
            tweet = decoded['text']
            d = datetime.datetime.now()
            c = d.strftime("%Y-%m-%d %H:%M:%S")
            t = tuple([tweet,c])
            with sqlite3.connect("test.db") as con:
                cur = con.cursor()    
                cur.execute("INSERT INTO tb(tweet,t_time) VALUES(?,?)",t)
                print
