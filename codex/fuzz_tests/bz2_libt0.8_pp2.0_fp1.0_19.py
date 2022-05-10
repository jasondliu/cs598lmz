import bz2
bz2_file = bz2.BZ2File("../conversation.csv.bz2")
with open("conversation.csv", "wb") as write_file:
    for line in bz2_file:
        write_file.write(line)


# In[3]:


# Set up the file to be read into a dataframe
df = pd.read_csv("../conversation.csv", names=["user_id", "conversation_id", "conversation_content", "conversation_timestamp", "status_id", "conversation_timestamp_original"], skiprows=1, encoding="utf8")
df = df.drop(columns=["conversation_timestamp_original"])

# Set up the file to be read into a dataframe
df_status = pd.read_csv("../status.csv", names=["status_id", "status_timestamp", "status_timestamp_original","status_type_id", "status_type", "user_id", "status_content"], skiprows=1, encoding="
