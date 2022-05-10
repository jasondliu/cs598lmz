import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\nPress Enter to continue...")).start()
input()

# As a simple example, we can use the list_files() method to list the files in the current working directory:

# In[2]:


from s3fs import S3FileSystem

s3fs = S3FileSystem()
s3fs.ls('s3://nyc-tlc/trip data/')


# The list_files() method has a few parameters that can help us narrow down the results. For example, we can use the kwarg recursive to only include results from the first level of the bucket:

# In[3]:


s3fs.ls('s3://nyc-tlc/trip data/', recursive=False)


# We can also use the kwarg detail to include the full metadata about the files in the output:

# In[4]:


for file in s3fs.ls('s3://nyc-tlc/trip data/', detail=True):
    print(file['Key'], file['Size'])


# If we want to list only
