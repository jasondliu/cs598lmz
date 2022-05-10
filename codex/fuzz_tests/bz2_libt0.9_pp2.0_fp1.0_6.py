import bz2
bz2.compress(msg)

def rand_generate(data):
    rand=random.randint(0, len(data)-1 )
    msg=data[rand].encode()
    return msg

#quick check for an error
elon_msg=msg[elon_index]

elon_rand_msg=rand_generate(msg)
#print (msg.index(elon_msg.decode()))
#print (msg.index(elon_rand_msg.decode()))


#import time

#now=time.time()

#future=now+15
#while time.time()<future:
#    print(time.time())
#    time.sleep(1)



def multiline_search(pattern,data):
    for line in data:
        if re.search(pattern, line):
            return line
phrase=re.compile(r'loves\sthe\s')
loves_the=multiline_search(phrase,msg)
#print (loves_the)

positive_msg
