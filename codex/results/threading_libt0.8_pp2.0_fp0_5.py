import threading
threading.stack_size(64*1024)
######
#
#
#
######
x=0
y=0
z=0
temp=0
######
#
#
#
######
def temp():
 global temp
 while True:
  temp=temperature()
  time.sleep(1)

def xacc():
 global x
 while True:
  x=read_accelerometer_x()
  time.sleep(1)

def yacc():
 global y
 while True:
  y=read_accelerometer_y()
  time.sleep(1)
 
def zacc():
 global z
 while True:
  z=read_accelerometer_z()
  time.sleep(1)

######
#
#
#
######
t=threading.Thread(target=temp)
t.daemon=True
t.start()
t1=threading.Thread(target=xacc)
t1.daemon=True
t1.start()
t2=threading.Thread(target=yacc)

