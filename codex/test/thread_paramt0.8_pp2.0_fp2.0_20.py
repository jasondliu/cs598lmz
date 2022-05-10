import sys, threading
threading.Thread(target=lambda:sys.stdout.write(str(raw_input())[::-1].lower()+"\n")).start()

#(lambda x:x.sort())(list(map(int,raw_input().split())))

#lambda x:print x,;reduce(lambda x,y:lambda:x()+y(),map(lambda x:lambda:sys.stdout.write(str(x)+"\n"),x))()

#reduce(lambda x,y:x+y,[1 if x=="o"or x=="k"or x=="u"else 2 for x in str(raw_input())])

#lambda x:x-x%4*2

#lambda x,y:x+y

#lambda x:sum(int(i)**2for i in str(x))

#print((lambda R,C:reduce(lambda x,y:x*y,map(int,raw_input().split(" ")),1))(*map(int,raw_input().split(" "))))

#lambda i:list(map(lambda x
