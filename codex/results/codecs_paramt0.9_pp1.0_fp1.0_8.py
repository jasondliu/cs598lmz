import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))

def my_func(str_input1,str_input2):
    return

if __name__=='__main__':
    str0=input() #读取空格分隔的两个字符串
    list1 = str0.split() #将输入转换为字符串列表
    str1=list1[0]
    str2=list1[1]
    str11=str1.decode('utf-8')
    str22=str2.decode('utf-8')
    len1=len(str11)
    len2=len(str22)
    allList=[]
    broList=[]
    i=0
    while i<len2:
        broList.append(0)
        i+=1
    i=0
    while i<len1:
        if str11[i]==str22[0]:
            broList
