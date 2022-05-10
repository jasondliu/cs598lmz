import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


# In[2]:


#sql_passwd = "jxq20160401"
#sql_user = "root"
#sql_host = "localhost"
#sql_db = "xueqiu"
#sql_port = 3306

sql_passwd = "123456"
sql_user = "root"
sql_host = "10.1.1.137"
sql_db = "xueqiu"
sql_port = 3306


# In[3]:


#sql_passwd = "jxq20160401"
#sql_user = "root"
#sql_host = "localhost"
#sql_db = "xueqiu"
#sql_port = 3306

#sql_passwd = "123456"
#sql_user = "root"
#sql_host = "10.1.1.137"
#sql_db = "xueqiu"
#sql_port = 3
