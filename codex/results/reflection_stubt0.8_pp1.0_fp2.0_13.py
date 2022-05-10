fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
'''

#python3.4中的漏洞:
# import os
# import marshal
# admin_cmds = ['adduser', "quit"]
# def get_command():
#     cmd = input('cmd:').strip()
#     return cmd
# if __name__ == '__main__':
#     while True:
#         cmd = get_command()
#         if len(cmd) == 0:
#             continue
#         if cmd in admin_cmds:
#             os.system(cmd)
#         else:
#             print("%s command not found." % cmd)
#             os.system('echo_command|python3')

#输入 'echo_command|python3' 运行该命令拿到__builtins__的字节序列

# def gen_cmd():
#     yield 'adduser'
#     yield "quit"
# marshal.dumps(gen_cmd) # 输出 b'\x80
