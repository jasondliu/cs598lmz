import mmap
import mmap_win

# List of included standard libraries
libs = ['stdio', 'stdlib', 'string', 'math', 'time', 'assert', 'ctype', 'errno', 'fcntl', 'locale', 'signal', 'setjmp']

# List of required system calls
syscalls = ['open', 'close', 'read', 'write', 'lseek', 'brk', 'rt_sigaction', 'rt_sigprocmask', 'exit_group', 'fstat', 'mmap', 'mprotect', 'munmap', 'pipe', 'dup', 'dup2', 'nanosleep']

# List of required instructions
required_instructions = ['mov', 'push', 'add', 'sub', 'call', 'ret', 'cmp', 'test', 'jmp', 'jl', 'jle', 'jg', 'jge', 'jz', 'jnz', 'jne', 'je', 'and', 'xor', 'or', 'shr', 'shl', 'imul', 'idiv', 'inc', 'dec',
