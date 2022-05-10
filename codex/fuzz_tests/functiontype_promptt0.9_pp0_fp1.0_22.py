import types
# Test types.FunctionType and types.LambdaType
def function_test(a):
    pass
print "function_test yra funkcija" if type(function_test) == types.FunctionType else "function_test nera funkcija"
lambda_test = lambda x: 2*x
print "lambda_test yra lambda funkcija" if type(lambda_test) == types.LambdaType else "lambda_test nera lambda funkcija"
#Funkcijos pozicionacios (ir asociacine) parametrai, namescpace - tai specifinis array\sąrašas 
#kuriame laikomi visi funkcijos argumentai(su kuria funckija perduodami)
def new_function(x,y=5,*args,**kwargs):
    print args
    print kwargs

new_function(1,2,3,4,5,6,a=7,b=8)

#Funkcijos calling - (funkcijos ekosvė) funkcijos su
