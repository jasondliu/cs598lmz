import codecs
codecs.encode(u'\U0001f4a9', 'unicode_escape').decode('utf-8')

print(codecs.encode(u'\U0001f4a9', 'unicode_escape'))


# In[56]:


# get emoji name
import emoji
print(emoji.emojize(':thumbs_up:'))
print(emoji.demojize('I like you :thumbs_up:'))
print(emoji.emojize(':thumbs_up_sign:'))
print(emoji.emojize(':+1:'))


# In[57]:


# remove emoji
import emoji
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U
