from types import FunctionType
list(FunctionType(fn,globals(),None))

def fn(a,b,c):
    print(a,b,c)

fn(1,2,3)
fn(1,2,3,4)
fn([1,2,3])
fn(*[1,2,3])

def fn(a,b=0,c=0):
    print(a,b,c)

fn(1,2,3)
fn(1,2)
fn(1)

def fn(a,*b):
    print(a,b)

fn(1,2,3)
fn(1,2)
fn(1)

def fn(a,**b):
    print(a,b)

fn(1,x=2,y=3)
fn(1,x=2)
fn(1)

def fn(a,b=0,*c,**d):
    print(a,b,c,d)

fn(1,2,3,4,x=5,y=6)
fn(1
