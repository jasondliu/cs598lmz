import threading
threading.stack_size(2 ** 27)

# Add threading and walk imports
import threading
import walk

# Set Input CSV file path
in_csv_path = "C:/Users/rcbotha/Desktop/in_csv/"

# Set Output CSV file path
out_csv_path = "C:/Users/rcbotha/Desktop/out_csv/"

# Set Filename as variable
filename = "media3.csv"

# Set Input CSV Filename
in_csv_name = in_csv_path + filename

# Set Output CSV Filename
out_csv_name = out_csv_path + "out_" + filename

# Set counter
counter = 0

"""
counter += 1
print(in_csv_name)
print(out_csv_name)
print(counter)


# In[15]:


csv_df = pd.read_csv(in_csv_name, encoding='utf-8-sig')
print(csv_df.head(1))


# In[12]:


walk.walk_csv(csv_df)
