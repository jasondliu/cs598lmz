import threading
threading.stack_size(67108864)


#---------------------

def topic_analysis(chunk,hashtag):
    #FILTER TODO
    #print("top analysis")
    for tweet in chunk[hashtag]:
        l = tweet.split(" ")
        for word in l:
            if "#"+hashtag == word:
                break
            if word not in chunk[hashtag]["freq"]:
                chunk[hashtag]["freq"][word] = 1
            else :
                chunk[hashtag]["freq"][word] += 1
    return chunk
#----------------------


def freq_analysis(chunk,result,lock):
    #FILTER TODO
    print("freq analysis")
    for hashtag in result :
        if hashtag not in chunk:
            chunk[hashtag] = {
                "freq":{},
                "presence":"NO TWEET TO ANALYSE"
            }
            chunk[hashtag]["presence"] = "NO TWEET TO ANALYSE"
        else :
            chunk
