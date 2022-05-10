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
del lst
del keepali0e[:]
'''

#gcc testcase on int/x86_64
GCC_CODE_AMD64 = '''
#include <stdio.h>
int main() {
    unsigned a = 0;
    while(a < 18446744073709551615UL) {
        a--;
    }
    printf("%llu",a);
}
'''

#gcc testcase on int/s390x
GCC_CODE_S390X = '''
#include <stdio.h>
int main() {
    unsigned long long a = 0;
    while(a < 40000000000000000000UL) {
        a--;
    }
    printf("%llu",a);
}
'''

#gcc testcase on int/ppc64
GCC_CODE_PPC64 = '''
#include <stdio.h>
int main() {
    unsigned long long a = 0;
    while(a < 18446744073709551615ULL) {

