import ctypes

class S(ctypes.Structure):
    x = ctypes.sizeof(ctypes.c_char_p)
    y = ctypes.sizeof(ctypes.c_void_p)

print S.x, S.y
</code>
Is there an easier way to define this C union in Python?
<code>union __pthread_mutex_s {
  struct __pthread_mutex_s *__next;
  int __spins;
  __pthread_list_t __list;
#if defined __x86_64__ || defined __i386__
  int __elision;
#endif
};
</code>
The <code>__list</code> field also has to be a union and is defined as:
<code>typedef union
{
  struct __pthread_mutex_s __data;
  char __size[__SIZEOF_PTHREAD_MUTEX_T];
  long int __align;
} pthread_mutex_t;
</code>
The <code>__next</code>, <code>__spins</code> and <code>__
