import bz2
bz2.BZ2File(filename).readlines()

#read the file into a list
#with open(filename, 'rb') as f:
#    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
#content = [x.strip() for x in content] 

content

#the data is a list of dictionaries
#each dictionary is a tweet
#the dictionary keys are the tweet attributes
#the dictionary values are the tweet values

#the first tweet in the list
#content[0]

#the date attribute of the first tweet
#content[0]['created_at']

#the text attribute of the first tweet
#content[0]['text']

#the user attribute of the first tweet
#content[0]['user']

#the screen_name attribute of the user attribute of the first tweet
#content[0]['user']['screen_name']

#the first tweet in the list
#content[0]

#the date attribute of the first tweet
#content[0
