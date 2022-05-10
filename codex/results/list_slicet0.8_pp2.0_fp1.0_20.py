import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
```

```
p=[]
while p:p.append(p)
```

```
#c++
using namespace std;
int main(){ int a[2] = { 1, 2 }; delete a; }
```

```
$ zsh -c 'cat /dev/zero' | zsh -c 'cat > /dev/null'
```

```
n=1;while : ;do n=$n+1;echo $n;done
```

```
for i in $(seq 100000); do echo 'while :; do if [ $(date +%s)%2 -eq 0 ]; then echo 1; else echo 0; fi; done' | bash; done
```

```
$ yes &
$ yes >/dev/full &
$ yes >/dev/full &
$ yes >/dev/full &
$ yes >/dev/full &
$ yes >/dev/full &
$ yes >/dev/full &
$ yes >/dev/full &
$ yes >/dev/full &
$ yes
